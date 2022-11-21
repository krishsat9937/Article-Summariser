all:
	docker build -t article_summariser:latest

run:
	docker run -p 5000:5000 article_summariser