# Futhon Programming Language
[![Build Status](https://travis-ci.org/rcmdnk/travis-test.svg?branch=master)](https://travis-ci.org/rcmdnk/travis-test)
[![Code Climate](https://codeclimate.com/github/delihiros/futhon/badges/gpa.svg)](https://codeclimate.com/github/delihiros/futhon)

Futhon is a programming language designed for Natural Language Processing and Machine Learning.

## Test

```
python setup.py test
```

## Example

```
(def np (import numpy))
(def chainer (import chainer))

(def x (np.array. [5]))

(def take
  (fn [n s]
    (if (or (neg? n) (empty? s))
      s
      (cons (first s)
            (take (dec n) (rest s))))))
```

## Primitives

![class](./resources/classes.png)

## Flow

![flow](./resources/flow.png)
