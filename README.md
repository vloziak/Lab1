# Відповіді на запитання :page_with_curl: :smiley:

**1. Що таке лінійні трансформації?**

**Лінійні трансформації**- це трансформації, які зберігають лінії координатної сітки паралельними та на однакових відстанях, тобто вони зберігають лінійну структуру простору.

**2. Як і в яких галузях застосовуються лінійні трансформації?**

Лінійні трансформації широко застосовуються у графіці, фізиці, інженерії, криптографії та інших галузях. Вони дозволяють виконувати зміщення, масштабування, обертання та інші операції з даними.

У фізиці лінійні трансформації використовуються для опису таких явищ, як обертання та відображення об’єктів у тривимірному просторі. Ці трансформації дозволяють нам зрозуміти, як змінюються координати об'єкта після застосування перетворення.

У техніці лінійні трансформації мають вирішальне значення для аналізу електричних кіл і систем керування. Вони дозволяють моделювати та маніпулювати електричними сигналами та аналізувати, як вони поводяться в різних умовах.

В інформатиці лінійні трансформації використовуються в обробці зображень і сигналів.

**3. Що таке матриця лінійної трансформації та як її можна інтерпретувати?**

**Матриця лінійної трансформації** - це трансформовані версії базисних векторів, які, зазвичай, зібрані в квадратну матрицю, яка представляє лінійне перетворення простору.

**4. Які особливості та властивості має матриця обертання?**

Під час її застосування вектор не змінить довжини, тому це означає, що ця матриця є ортогональною (її обернена матриця дорівнює транспонованій матриці). Також визначник цієї матриці дорівнює 1.

**5. Чи залежить фінальний результат від порядку трансформацій?**

Так, залежить. Ось приклад:

![example](https://github.com/vloziak/Lab1/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(120).png?raw=true)

**6. Як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію?**

Для знаходження оберненої трансформації потрібно знайти обернену матрицю трансформації, але обернена матриця існує лише для квадратних матриць, які є невиродженими(визначник = 0), тому не завжди все можна повернути до початкового вигляду.

**7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)?**

![example](https://github.com/vloziak/Lab1/blob/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(121).png?raw=true)

Визначник матриці трансформації є важливим числовим параметром, який надає інформацію про геометричні властивості лінійної трансформації.

- Det < 1:

Вектори стають ближчими один до одного після трансформації, що свідчить про стиснення простору. Прикладом такої трансформації може бути масштабування з коефіцієнтом менше 1, наприклад, зменшення розмірів об'єкта вдвічі. 

- Det > 1:

Вектори стають дальшими один від одного після трансформації, що свідчить про розтягування простору. Прикладом такої трансформації може бути масштабування з коефіцієнтом більше 1, наприклад, збільшення розмірів об'єкта вдвічі.

- Det = 1:

Якщо визначник дорівнює 1, це означає, що трансформація зберігає площу фігури. Це вказує на те, що трансформація є ізометрією, тобто зберігає відстані та кути між векторами, але може змінювати їхнє положення або напрямок. Прикладом такої трансформації може бути обертання або відбиття, яке не змінює розмірів об'єкта, але змінює його орієнтацію. В нашому випадку ми обернули зірку на 45 градусів.

- Det = 0:

Якщо визначник дорівнює 0, це означає, що трансформація зменшує простір до нижчої розмірності. Така трансформація не є оборотною і втрачає частину інформації про початковий простір. В нашому випадку ми з двохвимірного простору перейшли в одновимірний, і зірка стала просто лінією на вісі Ox.