![Pytholic logo](https://i.imgur.com/do67VC7.png)

# Pytholic

Develop and praise God at the same time!

## Description

My main goal with Pytholic is to show that we, Catholics, can praise God and teach about Him in any way possible. Just like what Saint Paul said in 1 Corinthians 10, 31: *"Whatever you eat, then, or drink, and whatever else you do, do it all for the glory of God."* My second goal with this project was to practice a different kind of penance other than feast and abstinence in this year's lent (I mean, programming is not a penance,  not for me, but doing it instead of play a game or watch a movie is).

## Instalation

```bash
 pip install pytholic
 ```

## Usage

Pytholic contains:
* The 4 gospels of the Bible.
* 12 prayers.
* 4 Icons as ASCII.
* A function that sanctify a string.
* A function that explains the doctrine of the Trinity.

The Bible class has 4 methods, matthew(), mark(), john() and luke(), they return a verse or a list of verses.
```python
from pytholic.bible.bible import Bible

bible = Bible()
# returns one verse
print(bible.matthew(1, 1))
# returns a list of verses
print(bible.matthew(1, 1, 5))
```
To return one of the 12 prayers.
```python
from pytholic.prayers import Prayers


prayer = Prayers()
# each prayer is a method that prints a string
prayer.our_father()
```
To return one of the 4 images.
```python
from pytholic.icons import IconAscii


icon = IconAscii()
# returns an Ascii representation of an icon
print(icon.pantocrator())
```
To sanctify a string.
```python
from pytholic.variety import sanctify


text = "Hello World, i'm Charles 5 and i'm cool guy :D"
sanctify(text)
```

To get an explanation of the Trinity.
```python
from pytholic.variety import trinity


# it will return a mini-game with a pythonic explanation of the Trinity
trinity()
```

## Contribute please 🇻🇦

As I said, this project was made as a form of penance, there's nothing special on it, but it can be improved. So if you are a catholic and a developer, please, consider helping this small project become something really great.

# *Viva Cristo Rei!*