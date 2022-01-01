package main

import (
	"log"
	"os"

	"github.com/streadway/amqp"
	cn "tinker.cf/rabbitmq/topic/common"
)

func main() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	cn.FailOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()
	ch, err := conn.Channel()
	cn.FailOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare("logs-topic", "topic", true, false, false, false, nil)
	cn.FailOnError(err, "Failed to declare an exchange")

	for i := 1; i <= 10000; i++ {
		body := cn.BodyFrom(os.Args, i)
		err = ch.Publish(
			"logs-topic",
			cn.RoutingKeyFrom(os.Args),
			false,
			false,
			amqp.Publishing{
				ContentType: "text/plain",
				Body:        []byte(body),
			},
		)
		cn.FailOnError(err, "Failed to publish message")
		log.Printf("[x] Sent %s", body)
	}

}
