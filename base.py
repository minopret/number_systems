# Write numbers in non-integer base,
# as given in Wikipedia "Non-integer representation" a/o 2011-07-15
# Impl: Aaron Mansheim, 2011-07-15/09-04
#
    # Would be sort of cool: also give answers in
    # Hehner-Horspool "quote notation" and in continued fractions;
    # and with balanced (pos/neg) digits if radix is odd integer.

from math import floor, fabs, log, modf

def floor_function(x):
    return floor(x)

def fractional_part(x):
    return fabs(modf(x)[0])

def _scaled_value(x, radix, place):
    # naive
    return x / radix**(place+1)

def _most_significant_place(x, radix):
    # most_significant_place k such that
    #   radix**k <= x < radix**(k + 1)
    # naive
    return floor_function(log(x, radix))

def to_non_integer_base(x, radix, truncation_place):
    # Enhancements that I'd like:
    # - include the radix in the representation,
    #   as perhaps "1;011(base 2)" to represent 1.375 decimal
    # - currently the truncation_place is the first place that does
    #   NOT appear in the output; consider carefully whether we may
    #   want it to be instead the last place that DOES appear
    # - produce an exponential notation when truncation_place > 0,
    #   as perhaps "1;011(base 2)*2^5" to represent 44 decimal
    # - reject unworkable radix such as 1, 0, -1
    # - permit suitable complex radix such as 2i
    # - limit precision (significant decimal digits)
    #   rather than accuracy (digits past the radix point)
    # - add a "from_non_integer_base" to reconvert the number to decimal
    # - show the arithmetic to reconvert the number to decimal,
    #   perhaps as columnar addition
    # - place a space between groups of five digits
    # - for rational numbers, figure out the length of the
    #   repetend and notate the repetend (this is much like quote notation).
    #   Refer to Euler's theorem.
    # Note: both quote notation and repetend notation
    #   use a lot of digits when a numerator is a relative prime to the radix
    # What to do about non-unique representation in a non-prime
    #   p-adic number system?

    representation = ''

    place = _most_significant_place(x, radix)
    if place < 0:
        place = 0        
    x = _scaled_value(x, radix, place)
    remainder = x
    
    while place > truncation_place:
        if place == -1:
            representation += ';'
        elif radix > 10:
            representation += ':'
        x = radix*remainder
        remainder = fractional_part(x)
        digit = int(floor_function(x))
        representation += str(digit)
        place = place - 1

    return representation

