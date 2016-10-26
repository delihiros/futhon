# Futhon Programming Language
[![Build Status](https://travis-ci.org/rcmdnk/travis-test.svg?branch=master)](https://travis-ci.org/rcmdnk/travis-test)
[![Code Climate](https://codeclimate.com/github/delihiros/futhon/badges/gpa.svg)](https://codeclimate.com/github/delihiros/futhon)

Futhon is a programming language designed for Natural Language Processing and Machine Learning.

## Test

```
python setup.py test
```

## Example

```clojure
(def np (import numpy))
(def chainer (import chainer))

(def l1 (chainer.links.Linear. 4 3))
(def l2 (chainer.links.Linear. 3 2))

(def my-forward
  (fn [x] (.__call__ l2 (.__call__ l1 x))))

(def x (.astype (np.array. [[1 2 3 4]]) (.float32 np)))

(.data (my-forward x))
; [[-1.02830815  0.6110245 ]]
```

## Primitives

![class](./resources/classes.png)

## Flow

![flow](./resources/flow.png)
