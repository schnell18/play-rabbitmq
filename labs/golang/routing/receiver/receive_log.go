package main

import (
	"fmt"
	"log"
	"os"

	"github.com/streadway/amqp"
	cn "tinker.cf/rabbitmq/routing/common"
)

func main() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	cn.FailOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()
	ch, err := conn.Channel()
	cn.FailOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare("logs-direct", "direct", true, false, false, false, nil)
	cn.FailOnError(err, "Failed to declare an exchange")

	q, err := ch.QueueDeclare("", false, false, true, false, nil)
	cn.FailOnError(err, "Failed to declare a queue")

	err = ch.Qos(200, 200, false)
	cn.FailOnError(err, "Failed to set Qos")

	for _, key := range os.Args[1:] {
		fmt.Printf("Bind exchange logs-direct and queue: %s with %s\n", q.Name, key)
		err = ch.QueueBind(q.Name, key, "logs-direct", false, nil)
		cn.FailOnError(err, "Failed to bind queue with exchange")
	}

	msgs, err := ch.Consume(
		q.Name,
		"",
		false,
		false,
		false,
		false,
		nil,
	)
	cn.FailOnError(err, "Failed to register consumer")

	forever := make(chan bool)

	go func() {
		for d := range msgs {
			log.Printf("[x]%s", d.Body)
		}
	}()

	log.Printf("[*] Wait for logs, CTRL-C to exit")
	<-forever
}
