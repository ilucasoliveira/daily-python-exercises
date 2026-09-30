from tasks import sum_number, slow_task

result_sum = sum_number.delay(1, 2, 3, 4)
result_slow = slow_task.delay(3)


print(result_sum.id)
print(result_sum.get())

print(result_slow.id)
print(result_slow.get())
