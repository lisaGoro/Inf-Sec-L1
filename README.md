# Проект: Шифр Цезаря

## Описание

Данный проект реализует шифр Цезаря. 
Шифр использует сдвиг букв в алфавите, в данном случае берется английский алфавит.
Проект включает функции для шифрования, дешифрования и взлома зашифрованного текста.

## Функционал

### Шифрование

Пользователь вводит текст и сдвиг, нажимает на соответствующую кнопку, после чего происходит шифрование текста.

Шифрование текста осуществляется путем сдвига каждой буквы на заданное количество позиций в алфавите.

### Дешифрование

Пользователь вводит зашифрованный текст и сдвиг, нажимает на соответствующую кнопку, после чего происходит дешифрование текста.

Дешифрование осуществляется с использованием обратного сдвига. 

### Взлом

Пользователь вводит зашифрованный текст и нажимает на соответствующую кнопку, после чего происходит взлом зашифрованного текста.

В проекте реализована функция для взлома шифра Цезаря. 
Она анализирует наиболее часто встречающуюся букву в тексте и сопоставляет ее с буквой «e», 
поскольку именно она является наиболее употребляемой в английском алфавите. 
Данные действия позволяют предположить величину сдвига и дешифровать текст.

## Примеры текста для шифрования


### 1

As young readers like to know ‘how people look’, we will take this moment to give them a little sketch of the four sisters, who sat knitting away in the twilight, while the December snow fell quietly without, and the fire crackled cheerfully within. It was a comfortable room, though the carpet was faded and the furniture very plain, for a good picture or two hung on the walls, books filled the recesses, chrysanthemums and Christmas roses bloomed in the windows, and a pleasant atmosphere of home peace pervaded it.

Отрывок из книги Луизы Мэй Олкотт «Маленькие женщины»

### 2

About half of the private flights taken between 2019 and 2023 were short—some under 100 miles—and could have been otherwise drivable trips, according to a new study in Communications Earth & Environment. 
Although only about 0.003 percent of the world’s population use private aviation, it is highly energy-intensive, emitting significantly more carbon per passenger than commercial flights. Celebrities in particular have faced growing criticism for their private aircraft use. 
Some private aircraft models might emit more carbon per hour than an average person emits in a year. As a result, those who regularly fly private can produce almost 500 times more carbon in a year compared to the average person  worldwide, according to the new study. 

Отрывок статьи «Private jets are increasingly replacing car trips—for the ultra-wealthy»

Источник: https://www.nationalgeographic.com/environment/article/private-jet-flights-climate-change