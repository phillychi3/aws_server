package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

var balance = 0

func main() {
	router := gin.Default()
	router.GET("/neko/", getneko)
	router.Run(":80")
}

// getBalance 取得帳戶內餘額
func getneko(context *gin.Context) {
	var msg = "https://www.nekos.fun/assets/img/neko_v2_332.jpg"
	context.JSON(http.StatusOK, gin.H{
		"messenger": "you did it",
		"status":    "ok",
		"neko":      msg,
	})
}
