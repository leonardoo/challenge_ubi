package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"
	"time"
	"github.com/julienschmidt/httprouter"
	"github.com/rs/cors"
)

var count = 0
var request_no = 0
var mux sync.Mutex

func addCount(add int){
	mux.Lock()
	count = count + add
	mux.Unlock()
}

func rootHandler(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
	addCount(1)
	defer addCount(-1)
	request_no = request_no + 1
	log.Println("new Request")
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, "ok")
	log.Println("Finish Request No: ", request_no)
}

func StatHandler(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, fmt.Sprintf("%d", count))
}

func SleepHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	addCount(1)
	defer addCount(-1)
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusCreated)
	millis := ps.ByName("millis")
	i, err := strconv.Atoi(millis)
	if err != nil{
		fmt.Fprint(w, fmt.Sprintf("Fail"))
		return
	}
	if i >= 1 && i <= 20000{
		t := time.Duration(i) * time.Millisecond
		time.Sleep(t)
		fmt.Fprint(w, fmt.Sprintf("%d", count))
	}else{
		fmt.Fprint(w, fmt.Sprintf("Fail"))
	}
}


func main() {
	c := cors.New(cors.Options{
		AllowedOrigins: []string{"*"},
		AllowedMethods: []string{"GET", "POST", "DELETE", "PUT", "OPTIONS"},
		AllowedHeaders: []string{"*"},
	})
	router := httprouter.New()
    router.GET("/", rootHandler)
    router.GET("/check/:millis", SleepHandler)
    router.GET("/stats", StatHandler)
	log.Println("Running")
	log.Fatal(http.ListenAndServe(":8080", c.Handler(router)))
}
