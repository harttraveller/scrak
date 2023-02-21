# kamaji

An asynchronous web scraping framework.


## Usage

```python
client = Client(verbose, agent)

client.run(urls) -> Task
```

The agent is a class which handles the returned web data.

A task is the returned object which contains status information, success, etc.


You can also start an api which allows you to submit tasks to the endpoint, which allows the API instance to adaptively learn the best way to submit information, optimizing either for speed, or success rates, or both.