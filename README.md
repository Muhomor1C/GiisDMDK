# GiisDMDK

  <h2>GiisDMDK</h2>
<p><a href="#anchor1">Russian</a></p>
<p><a href="#anchor2">Polski</a></p>
<p><a href="#anchor3">English</a></p>

![IMG_20220609_235425883](https://user-images.githubusercontent.com/86445162/172951919-2e6c9c4d-25aa-4bb7-930a-83f0175b0822.jpg)

![IMG_20220610_003542349](https://user-images.githubusercontent.com/86445162/172956591-f4222b20-af57-4a02-9c47-0d002e2a46b6.jpg)

![IMG_20220610_004024628](https://user-images.githubusercontent.com/86445162/172957075-bf290e92-0300-41ac-8a32-d0f51f92d727.jpg)


<p id="anchor1">Russian</p>
<p>Консольная утилита печати контрольных марок для ювелирных изделий на принтере этикеток.

Задача:
  Необходимо напечатать этикетки для ювелирных изделий, которые поступили в розничный оборот до 31.12.21(до
введения обязательной маркировки на предприятиях изготовителях. Т.Н. - остатки)
Имеется XLS файл с полученными из государственной инрформационной системы контроля за драг. металлами и драг. камнями (ГИИС ДМДК)
уникальными идентификационными кодами(УИН). Необходимо сопоставить эти номера со штрихкодами изделий в формате EAN13
и написать утилиту для изготовления этикеток с этим УИН в виде DataMatrix кода.

Решение:
  У клиента имеется в наличии принтер этикеток TSC TDP-225, который и был взят за основу.
Подключена библиотека SDK TSCLIB.dll, с помощью которой налажено прямое управление принтером
минуя диспетчер печати Windows.

Файлы с данными о товаре из "1С:Ювелирный магазин", были переведены в CSV для быстроты и удобства работы и сопоставлены с данными из ГИИС.
В итоге получил файл END.CSV, в котором имеется все необходимое. Эта работа не отражена в репозитории. Желающим могу вылсать утилиту,
написанную для этого.

  В конечном итоге, работник сканирует заводской ярлык изделия и принтер автоматически печатает этикетку с УИН кодом
в виде DataMatrix. Кроме того, на этикетке печатается наименование изделия, общий вес и отдельно вес драг. металлов, оригинальный
штрихкод и линия сгиба, по которой этикетка наклеивается на контрольную нить изделия.
При должной сноровке, печать и поклейка этикетки занимает не более 10 секунд, что немаловажно, учитывая количество
товара(тысячи позиций в нескольких магазинах сети клиента).

Порядок полей в CSV файле:

0 - внутренний ID товара(не обязателен для заполнения)

1 - УИН

2 - Наименование

3 - Общий вес

4 - Вес металла

5 - Штрихкод


Этикетка 30*20 мм. Склеивается пополам, получается маленький, аккуратный ярлычек.


  Что не сделано(TODO):
  Утилита должна работать на всех принтерах TSC, но проверить нет возможности из за отсутствия техники. Как и нет возможности 
  поэксперементировать с другими производителями.
  Формат и размер этикетки жестко настроен в программе. Возможно когда то я доработаю этот момент.
  Было бы не плохо привинтить UI, но категорически нехватает времени
</p>
  




<p id="anchor2">Polski</p>
<p>
Narzędzie konsoli do drukowania znaczków kontrolnych biżuterii na drukarce etykiet.

Zadanie:
Konieczne jest wydrukowanie etykiet na biżuterię, które weszły do obrotu detalicznego przed 31.12.21 (do
wprowadzenie obowiązkowego oznakowania w przedsiębiorstwach producentów. TN-resztki)
Istnieje plik XLS z uzyskanymi z państwowego systemu inrformacyjnego kontroli drag. metalami i drag. kamieniami (GIS DMDK)
unikalnymi kodami identyfikacyjnymi (UIN). Musisz dopasować te numery do kodów kreskowych produktów w formacie EAN13
i napisać narzędzie do tworzenia etykiet z tym UIN w postaci kodu DataMatrix.

Decyzja:
Klient posiada drukarkę etykiet TSC TDP-225, która została przyjęta jako podstawa.
Dołączona jest biblioteka SDK TSCLIB.dll, za pomocą którego skonfigurowano bezpośrednie sterowanie drukarką
pomijając menedżera drukowania systemu Windows.

Pliki z danymi produktu z "1C: Sklep jubilerski" zostały przetłumaczone na CSV dla szybkości i wygody pracy i porównane z danymi z GIS.
W końcu dostałem plik END.CSV, który ma wszystko, czego potrzebujesz. Ta praca nie jest odzwierciedlona w repozytorium. Chętnym mogę wyłowić narzędzie,
napisane w tym celu.

Ostatecznie pracownik skanuje Etykietę fabryczną produktu, a drukarka automatycznie drukuje etykietę z kodem UIN
tak jak DataMatrix. Ponadto na etykiecie drukowana jest nazwa produktu, Waga całkowita i oddzielnie waga drag. metali, oryginalny
Kod kreskowy i linia zagięcia, wzdłuż której etykieta jest przyklejona do nici kontrolnej produktu.
Przy odpowiednich umiejętnościach drukowanie i klejenie etykiety zajmuje nie więcej niż 10 sekund, co jest ważne, biorąc pod uwagę ilość
towaru (tysiące pozycji w kilku sklepach sieci klienta).

Kolejność pól w pliku CSV:

0-wewnętrzny identyfikator towaru(nie wymagany do wypełnienia)

1-UIN

2-Nazwa

3-Waga całkowita

4-waga metalu

5-Kod kreskowy


Etykieta 30 * 20 mm. przyklejona na pół, okazuje się, że jest to mała, zgrabna Etykieta.


Czego nie zrobiono(TODO):
Narzędzie powinno działać na wszystkich drukarkach TSC, ale nie ma możliwości sprawdzenia z powodu braku techniki. Jak nie ma możliwości
poeksperymentuj z innymi producentami.
Format i rozmiar etykiety jest zakodowany w programie. Może kiedyś sfinalizuję ten moment.
Nie byłoby źle przykręcić UI, ale kategorycznie brakuje czasu
</p>
<p id="anchor3">English</p>
