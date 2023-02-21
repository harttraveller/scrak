# kamaji

An asynchronous web scraping framework built around [scrapestack](https://scrapestack.com). The name derives from the character "Kamaji" in studio ghiblis "Spirited Away".

The idea behind this package is that instead of submitting a request directly, you submit the requests to a "bucket" that is maintained by a local flask application. The backend of this program manages asynchronous web request submission, and upon successfully receiving data, it deposits it in a collection bucket, which the user can then collect at their own pace.

The benefit of the "bucket" paradigm is that the application can optimize the rate at which requests are handled by dynamically adjusting the request timeout, allowing some requests to drop and be rerun.

## Usage

```python
client = Client(verbose, agent)

client.run(urls) -> Task
```

```
# you must start the API for this to work
kamaji = Kamaji()

kamaji.run(urls) -> Task
```

The agent is a class which handles the returned web data.

A task is the returned object which contains status information, success, etc.

You can also start an api which allows you to submit tasks to the endpoint, which allows the API instance to adaptively learn the best way to submit information, optimizing either for speed, or success rates, or both.