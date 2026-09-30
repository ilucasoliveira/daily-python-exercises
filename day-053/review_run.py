from review_tasks import unstable_task, process_data

result_unstable = unstable_task.delay(10)
result_process = process_data.delay([1, 2, 3, 4, 5])

print("instable id:", result_unstable.id)
print("process id:", result_process)
print("process result:", result_process.get())
