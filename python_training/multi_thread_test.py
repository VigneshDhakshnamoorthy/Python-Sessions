import concurrent.futures
import time

start = time.perf_counter()


def multi_thread():
    print('Started')
    time.sleep(1)
    return 'Ended'


with concurrent.futures.ThreadPoolExecutor() as executor:
    result = [executor.submit(multi_thread) for _ in range(100)]

    for f in concurrent.futures.as_completed(result):
        print(f.result())

end = time.perf_counter()

print(f"Took {round(end - start, 3)} Second's to Complete")
