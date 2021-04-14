# Antivirus
The new system for the Reply Code Challenge works great, but R-Boy is not so convinced... It seems
in fact that the famous mascot of Reply sniffed a virus hidden among the files sent by a participant!

We know the length of the virus and we know that it repeats the same in the four files we received,
but we do not know where. Help us to identify the virus!

### Details
The four files F[1], F[2], F[3], F[4] are input data, represented as four character strings of length,
respectively N[1], N[2], N[3], N[4].

The virus is a string of characters V of length M. The length M is an input data, but the contents of
the V string of the virus are not known.

We know with certainty that the V virus appears within all four files, as a sub-string of consecutive
characters. We also know that there are not other consecutive substrings of length M that are
repeated the same in all four files.

The positions of the characters in the strings are numbered starting from 0. For each of the four F[i]
files, find the location where the virus is inserted, which is the location where the first character of
the V virus appears within the F[i] string.

### Assumptions
- T <= 1.000, the number of test cases.
- 2 <= N[1], N[2], N[3], N[4] <= 1.000, the files are not longer than 1000 characters.
- 2 <= M <= 1.000, the virus is not longer than 1.000 characters.
- M <= min(N[1], N[2], N[3], N[4]), the virus is not longer than the shortest file.
- All file characters are lowercase letters of the English alphabet (from a toz), no spaces are present.
- It is guaranteed that the virus exists and is unique.

### Input data
The first line of the input file contains an integer T, the number of test cases. Followed by T test
cases, numbered from 1 to T.

In each test case: - The first line contains four integer separated by spaces N[1], N[2], N[3], N[4],
the lengths of each of the four files. - The second line contains only the integer M, the length of the
virus. - The following 4 lines contain the four strings F[1], F[2], F[3] and F[4] respectively.

### Output data
The output file must contain the answer to the test cases you could solve. For each test case you've
solved, the output file must contain a line with the words:

>Case #t: p1 p2 p3 p4

where t is the test case number (starting from 1) and the values p1,p2, p3,p4 are the locations where
the virus is located in each of the four file. Position means the index of the first character of the
virus, the first character of the file has zero index.

## Example of input/output
### Input:
```
2
8 12 10 7
4
ananasso
associazione
tassonomia
massone

6 9 11 10
3
simone
ponessimo
milionesimo
cassonetto
```
### Output:
>Case #1: 4 0 1 1

>Case #2: 3 1 4 4

### Explanation
- In the first example case the virus is asso: ananasso, associazione, tassonomia, massone.
- In the second example case the virus is one: simone, ponessimo, milionesimo, cassonetto
