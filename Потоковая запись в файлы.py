import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()

print(end_time-start_time)

start_time2 = time()

threads = []
args = [(10, 'example5.txt'),
        (30, 'example6.txt'),
        (200, 'example7.txt'),
        (100, 'example8.txt')]

for x in args:
    thread = threading.Thread(target=write_words, args=x)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time2 = time()

print(end_time2-start_time2)