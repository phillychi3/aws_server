package main

import (
	"net"
	"os"

	b64 "encoding/base64"
)

const (
	RECV_BUF_LEN = 1024
)

func main() {
	println("啟動伺服器~~")
	println("port設定:6666")

	listener, err := net.Listen("tcp", ":6666")
	if err != nil {
		println("監聽錯誤：", err.Error())
		println("關閉伺服器。")
		os.Exit(1)
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			println("連線錯誤：", err.Error())
			continue
		}
		go ClientLogic(conn)
	}
}

func ClientLogic(conn net.Conn) {

	buf := make([]byte, RECV_BUF_LEN)
	n, err := conn.Read(buf)
	if err != nil {
		println("阿哩 接收出問題了", err.Error())
		return
	}
	println("接收到了 ", n, "byte  資料：", string(buf))
	data := string(buf)
	sDec, _ := b64.StdEncoding.DecodeString(data)
	println(sDec)
	_, err = conn.Write([]byte(sDec))
	if err != nil {
		println("發送失敗：", err.Error())
	} else {
		println("發送成功")
	}

	conn.Close()
}
