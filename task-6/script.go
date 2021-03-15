package main

import (
	"context"
	"fmt"
	"log"

	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main(){
	if err := run(); err != nil {
		log.Fatal(err)
	}
}

func run() (err error) {
	withCredentials := reddit.WithCredentials("pe*********A","	w8******************A","srikesh322", "*************")
	client, _:= reddit.NewClient(withCredentials)

	Subreddit, _,err := client.Subreddit.SearchNames(ctx,"memes")
	if err != nil {
		return
	}
  
  	fmt.Printf("\n List of Subreddit when memes is in search query.\n\n")

	var s []string
	for _, Subreddit := range Subreddit{
		fmt.Println(Subreddit)
		s = append(s, Subreddit)
	}

	posts, _,err := client.Subreddit.TopPosts(ctx, "memes", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
		},
		Time: "week",
	})
  
  	if err != nil{
		return
	}
  
  	return
}
