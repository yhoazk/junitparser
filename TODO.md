- Need to Research how junit 5 report format has changed

- Tag support
- Unique ID support and usage

For reference: Jenkins still displays function names in report, but
extracts unique-id and display-name to case standard output:
https://junit.ci.cloudbees.com/job/JUnit5/lastCompletedBuild/testReport/example/DisplayNameDemo/

Also I may have to use lxml since the battery parser ignores comments.

- Prompt user if they don't have lxml

- Also, tests.

