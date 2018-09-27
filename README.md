парсилка

<h3><b>Описание</b></h3>
    <p>1. requester.py . - делает запросы по выбранному урлу и возвращает значение</p>
    <p>2. breed_parser.py - парсит все категории пород с avito .ru/moskva/koshki и возвращает dict</p>
    <p>3. main_parser.py - ходит по страничкам вида avito. ru/moskva/koshki/порода?p=NUM и парсит инфу из блоков объявленией
    сейчас это id объявления, url на основную страничку объявления, url на тамб и породу
    все это записывается в csv(по дефолту cats_avito.csv)
    ходит нежно и аккуратно и медленно</p>
    <div>4. ad_parser.py  - принимает url на объявления из main_parser.py, делает туда реквесты, и записывает полученные данные в 
     формате</div>  
     <div>
  <ul>
        <li>'id'</li>
        <li>'title'</li>
        <li>'title'</li>
        <li>'date'</li>
        <li>'image_url'</li>
        <li>'price'</li>
        <li>'address'</li>
        <li>'desc'</li>
        <li>'breed'</li> 
  </ul>
    </div>
        <div>в csv
        возможно 4к объявлений будет парсится больше одного дня, возможно все данные будут браться из main_parser.py( тогда увы description будет обрезан)</div>
