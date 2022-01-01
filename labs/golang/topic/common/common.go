package common

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func FailOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}

func RoutingKeyFrom(args []string) string {
	var s string
	if len(args) < 2 || os.Args[1] == "" {
		s = "info.order"
	} else if len(args) < 3 || os.Args[2] == "" {
		s = fmt.Sprintf("%s.order", os.Args[1])
	} else {
		s = fmt.Sprintf("%s.%s", os.Args[1], os.Args[2])
	}
	return s
}

func BodyFrom(args []string, i int) string {
	var s string
	if len(args) < 2 || os.Args[1] == "" {
		s = "hello"
	} else {
		s = strings.Join(args[1:], " ")
	}
	return fmt.Sprintf("%s[%d]", s, i)
}
