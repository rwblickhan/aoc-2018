#lang racket

(require racket/set)

(define in (map string->number (string-split (port->string (open-input-file "input")))))

(pretty-print (foldl + 0 in))

(define (loop-freqs seen-set acc)
  (loop-freqs-helper in seen-set acc))

(define (loop-freqs-helper freqs seen-set acc)
  (let ([new-acc (+ acc (first freqs))])
    (if (set-member? seen-set new-acc)
      new-acc
      (if (empty? (rest freqs))
        (loop-freqs (set-add seen-set new-acc) new-acc)
        (loop-freqs-helper (rest freqs) (set-add seen-set new-acc) new-acc)))))

(pretty-print (loop-freqs (set 0) 0))
