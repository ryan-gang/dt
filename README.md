# TODO
1. cli interface
2. github integration
3. llm integration
4. minimal timesheet integration
5. linear integration

```
# by default only github stats
dt today
dt yesterday
dt 2025-05-01
# llm summarizer
dt today --summarize
# use linear/github integration
dt today -l -g --summarize
```

# Timesheet
Only on-disk storage, no in memory persistence.
New new files for every month. 
Store in ~/Developer/timesheets/2025/may.csv
Rows: Project, Description, Tags, Start DateTime, End DateTime, Duration

- Project: can be just the repo name
- Description: task description (Linear ID / gh PR ID)
- Tags: #code-review, #research, #planning, #implementation, #bug-squashing
- Start DateTime: auto
- End DateTime: auto
- Duration: always computed

```
dt start <project> <description> <tags>
# should pause the currently running task
dt pause
# should end the currently running task
dt stop
dt log <project> <description> <tags> <start> <end>
```