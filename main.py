import csv
import os
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from gen import gen
from timsort import timsort

bg="#111111"
fg="#ffd6ec"
pk="#ff4fa3"
pk2="#ff8cc6"
gr="#503040"


def rd(p):
	with open(p,"r",encoding="utf-8") as f:
		s=f.read().strip()
	if not s:
		return []
	return list(map(int,s.split()))


def one(p):
	a=rd(p)
	b=a[:]
	t1=time.perf_counter()
	st=timsort(b)
	t2=time.perf_counter()
	return len(a),t2-t1,st


def save_csv(rows):
	with open("out/res.csv","w",newline="",encoding="utf-8") as f:
		w=csv.writer(f)
		w.writerow(["file","n","t","st"])
		for r in rows:
			w.writerow(r)


def draw(rows):
	ns=[x[1] for x in rows]
	ts=[x[2] for x in rows]
	ss=[x[3] for x in rows]
	plt.rcParams.update({
		"figure.facecolor":bg,
		"axes.facecolor":bg,
		"savefig.facecolor":bg,
		"text.color":fg,
		"axes.labelcolor":fg,
		"axes.edgecolor":fg,
		"xtick.color":fg,
		"ytick.color":fg,
		"grid.color":gr,
	})
	plt.figure(figsize=(9,5))
	plt.plot(ns,ts,color=pk,marker="o",markersize=3,linewidth=1.5)
	plt.title("Timsort: time(n)")
	plt.xlabel("n")
	plt.ylabel("sec")
	plt.grid(True,linestyle="--",alpha=0.6)
	plt.tight_layout()
	plt.savefig("out/time.png",dpi=220)
	plt.close()
	plt.figure(figsize=(9,5))
	plt.plot(ns,ss,color=pk2,marker="o",markersize=3,linewidth=1.5)
	plt.title("Timsort: steps(n)")
	plt.xlabel("n")
	plt.ylabel("steps")
	plt.grid(True,linestyle="--",alpha=0.6)
	plt.tight_layout()
	plt.savefig("out/steps.png",dpi=220)
	plt.close()


def tbl(rows,k=15):
	s=[]
	s.append("| file | n | t | st |")
	s.append("|---|---:|---:|---:|")
	for f,n,t,st in rows[:k]:
		s.append(f"| {f} | {n} | {t:.6f} | {st} |")
	return "\n".join(s)


def txt_code(p):
	with open(p,"r",encoding="utf-8") as f:
		return f.read().strip()


def report(rows):
	ns=[x[1] for x in rows]
	ts=[x[2] for x in rows]
	ss=[x[3] for x in rows]
	i1=ns.index(min(ns))
	i2=ns.index(max(ns))
	avg_t=sum(ts)/len(ts)
	avg_s=sum(ss)/len(ss)
	s=f"""Семестровая работа
Алгоритм сортировки Timsort

1. Название алгоритма и краткая историческая справка
В этой работе рассматривается алгоритм сортировки Timsort
Его придумал Tim Peters в 2002 году для Python
Этот алгоритм используется в Python как стандартная сортировка
Его сделали для того, чтобы сортировка работала быстро
и нормально показывала себя на реальных данных

2. Описание принципа работы и особенностей
Timsort это гибридный алгоритм сортировки
Он сочетает insertion sort и merge sort

Сначала массив делится на маленькие части
В программе размер части это 32 элемента
Каждая такая часть сортируется через insertion sort
Потом все эти части постепенно сливаются между собой

Из за этого алгоритм работает довольно удобно
Маленькие куски быстро сортируются
А большие данные потом соединяются через слияние

Еще Timsort является стабильной сортировкой
То есть одинаковые элементы не теряют свой порядок

3. Оценка сложности алгоритма
Сложность в лучшем случае O(n)
Сложность в среднем случае O(n log n)
Сложность в худшем случае O(n log n)
Дополнительная память O(n)

Лучший случай бывает тогда, когда данные уже
частично упорядочены
В среднем и в худшем случае рост идет
примерно как n log n

4. Генерация входных данных
Было создано 100 файлов со случайными массивами
Размер массивов от 100 до 10000 элементов
Все файлы лежат в папке data

5. Измерение времени и шагов
Для каждого файла массив сначала считывался
Потом отдельно запускалась сортировка
Время чтения файла в замер не входило

Считались два показателя
Время выполнения сортировки
Количество шагов внутри сортировки

6. Средние значения
Минимальный размер массива {ns[i1]}
Время для него {ts[i1]:.6f} секунд
Количество шагов {ss[i1]}

Максимальный размер массива {ns[i2]}
Время для него {ts[i2]:.6f} секунд
Количество шагов {ss[i2]}

Среднее время сортировки {avg_t:.6f} секунд
Среднее количество шагов {avg_s:.2f}

7. Сравнение теории и практики
По теории Timsort должен работать
примерно как O(n log n)
По графикам видно, что при росте размера массива
время и количество шагов тоже растут
Графики не идеально ровные, потому что данные случайные
Но в целом результат получился нормальный
и довольно близкий к теории

8. Таблица результатов
Ниже показаны первые 15 строк
Полная таблица лежит в файле out/res.csv

{tbl(rows)}

9. Графики
График времени: out/time.png
График шагов: out/steps.png

10. Вывод
В этой работе был реализован алгоритм Timsort на Python
Потом была сделана генерация входных данных
Дальше были измерены время и количество шагов
По результатам видно, что алгоритм работает быстро
и с увеличением размера массива нагрузка растет ожидаемо
То есть практика тут в целом совпала с теорией

11. Источники
1. Python Documentation
2. Материалы по алгоритмам сортировки
3. Описание алгоритма Timsort

12. Код алгоритма
```python
{txt_code("timsort.py")}
```

13. Код генерации входных данных
```python
{txt_code("gen.py")}
```

14. Приложение
Входные данные лежат в папке data
Там 100 файлов со случайными массивами
"""
	with open("report.md","w",encoding="utf-8") as f:
		f.write(s)
	with open("report.txt","w",encoding="utf-8") as f:
		f.write(s)


def prs(rows):
	ns=[x[1] for x in rows]
	ts=[x[2] for x in rows]
	ss=[x[3] for x in rows]
	i1=ns.index(min(ns))
	i2=ns.index(max(ns))
	s=f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Timsort</title>
<style>
body{{margin:0;background:#000;color:#ffd6ec;font-family:Consolas,'Courier New',monospace;overflow:hidden}}
.sl{{display:none;box-sizing:border-box;padding:40px 54px;height:100vh;background:#000}}
.on{{display:block}}
h1,h2{{color:#ff4fa3;margin:0 0 18px}}
p,li{{font-size:26px;line-height:1.35}}
ul{{margin:18px 0 0 24px}}
.sm{{font-size:22px;color:#ffb8da}}
.bx{{border:2px solid #ff4fa3;border-radius:18px;padding:18px 22px;background:#120710}}
img{{max-width:100%;max-height:62vh;border:2px solid #ff4fa3;border-radius:18px}}
.n{{position:fixed;right:18px;bottom:12px;color:#ff8cc6;font-size:16px}}
pre{{margin:0;background:#120710;border:2px solid #ff4fa3;border-radius:18px;padding:16px;color:#ffd6ec;font-size:17px;line-height:1.25;white-space:pre-wrap}}
</style>
</head>
<body>
<section class="sl on"><h1>Timsort</h1><p>Сортировка массивов на Python</p><p class="sm">Черный фон и розовая тема</p></section>
<section class="sl"><h2>Коротко про алгоритм</h2><ul><li>Timsort придумал Tim Peters</li><li>он используется в Python</li><li>это гибрид insertion sort и merge sort</li><li>алгоритм удобен для реальных данных</li></ul></section>
<section class="sl"><h2>Как он работает</h2><ul><li>массив делится на маленькие части</li><li>каждая часть сортируется вставками</li><li>потом части сливаются между собой</li><li>в работе считались время и шаги</li></ul></section>
<section class="sl"><h2>Сложность</h2><div class="bx"><p>лучший случай O(n)</p><p>средний случай O(n log n)</p><p>худший случай O(n log n)</p><p>память O(n)</p></div></section>
<section class="sl"><h2>Что было сделано</h2><ul><li>создано 100 файлов со случайными массивами</li><li>размеры от 100 до 10000</li><li>чтение файла не входило в замер</li><li>графики строились через matplotlib</li></ul></section>
<section class="sl"><h2>Результаты</h2><ul><li>мин размер {ns[i1]}</li><li>макс размер {ns[i2]}</li><li>среднее время {sum(ts)/len(ts):.6f} сек</li><li>среднее число шагов {sum(ss)/len(ss):.2f}</li></ul></section>
<section class="sl"><h2>График времени</h2><img src="out/time.png" alt="time"></section>
<section class="sl"><h2>График шагов</h2><img src="out/steps.png" alt="steps"></section>
<section class="sl"><h2>Код алгоритма</h2><pre>{txt_code("timsort.py")}</pre></section>
<section class="sl"><h2>Код генерации данных</h2><pre>{txt_code("gen.py")}</pre></section>
<section class="sl"><h2>Вывод</h2><ul><li>при росте n время растет</li><li>количество шагов тоже растет</li><li>практика получилась близка к O(n log n)</li><li>алгоритм реально удобный для массивов</li></ul><p class="sm">Листать стрелками</p></section>
<div class="n" id="n"></div>
<script>
let i=0
let a=[...document.querySelectorAll('.sl')]
let n=document.getElementById('n')
function sh(){{a.forEach((x,j)=>x.classList.toggle('on',i===j));n.textContent=(i+1)+' / '+a.length}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' ' ){{i=(i+1)%a.length;sh()}} if(e.key==='ArrowLeft'){{i=(i-1+a.length)%a.length;sh()}}}})
sh()
</script>
</body>
</html>
"""
	with open("presentation.html","w",encoding="utf-8") as f:
		f.write(s)


def speech():
	s="""Текст для озвучки

Всем привет
В этом видео показана работа по теме алгоритма сортировки Timsort
Он был выбран потому что используется в самом Python
и сам по себе он выглядит интереснее обычных сортировок

Если коротко, Timsort это смесь insertion sort и merge sort
Сначала массив делится на маленькие части
Потом эти части сортируются
А дальше уже соединяются между собой

Для этой работы данные не вводились руками
Была сделана генерация и создано 100 файлов
В каждом файле лежит свой случайный массив
Размеры были от 100 до 10000 элементов

Потом сортировка запускалась для каждого файла
Важно, что замерялась только сама сортировка
Чтение из файла в замер не входило

Считались два показателя
Первое это время выполнения
Второе это количество шагов внутри алгоритма

По графику времени видно
что чем больше массив, тем больше времени нужно
По графику шагов примерно то же самое
То есть поведение вполне ожидаемое

По теории у Timsort лучший случай O n
А средний и худший случаи O n log n
По полученным результатам практика на это похожа
Графики не идеально ровные
но общий рост выглядит нормально

В презентацию также добавлен код алгоритма
и код генерации входных данных
Чтобы было видно, что работа реально сделана

Если смотреть на итог
то Timsort показал себя как удобный и быстрый алгоритм
Особенно если работать с массивами

На этом все
Спасибо за внимание
"""
	with open("video_text.txt","w",encoding="utf-8") as f:
		f.write(s)


def main():
	if not os.path.isdir("data") or len(os.listdir("data"))<100:
		gen()
	os.makedirs("out",exist_ok=True)
	rows=[]
	fs=sorted([x for x in os.listdir("data") if x.endswith(".txt")])
	for f in fs:
		n,t,st=one(os.path.join("data",f))
		rows.append([f,n,t,st])
	rows.sort(key=lambda x:x[1])
	save_csv(rows)
	draw(rows)
	report(rows)
	prs(rows)
	speech()
	print("ok")


if __name__=="__main__":
	main()
