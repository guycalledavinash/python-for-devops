# Loops

## Retry logic

Retry logic repeats an operation after a temporary failure. Retries are useful in DevOps automation because a short-lived issue can clear on its own without failing the whole task.

In `05-retry-example.py`, `max_attempts` sets the maximum number of tries and `delay` sets the number of seconds to wait between failed attempts. The simulated operation fails twice and succeeds on its third attempt.

Run the example from the repository root:

```bash
python Day-09/05-retry-example.py
```
