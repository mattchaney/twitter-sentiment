# twitter-sentiment

A basic Twitter sentiment analysis app.

The architecture is based on an [AWS Compute Blog Post](https://aws.amazon.com/blogs/compute/from-poll-to-push-transform-apis-using-amazon-api-gateway-rest-apis-and-websockets/) 
that outlines a better way to handle rendering the results of long-running asynchronous tasks in web apps using websockets and AWS Step Functions.

## TODO

- serverless configuration
    - state machine configuration
        - DONE
    - lambda environment variables
        - stepfunctions_arn
            - OpenConnection
            - SendResponse
        - callbackURL - e.g. `https://ebscxgnb5g.execute-api.us-east-1.amazonaws.com/prod`
            - SendResponse
        - data_bucket_arn
            - GetTweets
            - GetSentiments
            - AggregateSentiments
    - add per-function IAM statements to limit access scope
- code each lambda
- automatic deployment
- dynamically set websocket and rest api endpoint in app index.html
