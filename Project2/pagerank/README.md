# pagerank

The program implements the PageRank algorithm, which is used to estimate the importance of web pages based on their link structure. Here is an explanation of the main structure and functionality of the code:

1. `crawl(directory)`: This function takes a directory name as input, parses HTML pages within the directory, extracts hyperlinks from each page, and builds a dictionary. Each page serves as a key in the dictionary, and the corresponding value is a set of other pages in the corpus that the key page links to.

2. `transition_model(corpus, page, damping_factor)`: This function returns a probability distribution over the next page to visit, given the current page, damping factor, and the structure of the corpus. The damping factor adjusts the probability of random jumping during the recursive process.

3. `sample_pagerank(corpus, damping_factor, n)`: This function estimates PageRank values for each page by performing random sampling based on the transition model. It starts from a random page, selects the next page according to the transition model, and repeats this process for a specified number of samples (n). The result is a dictionary where keys are page names, and values are the estimated PageRank values, ranging from 0 to 1 and summing to 1.

4. `iterate_pagerank(corpus, damping_factor)`: This function calculates PageRank values for each page by iteratively updating the values until convergence. It initializes PageRank values for each page and iteratively updates them based on the transition model and existing PageRank values. Convergence is achieved when the change in PageRank values falls below a small threshold (EPS). The result is a dictionary with page names as keys and estimated PageRank values as values, ranging from 0 to 1 and summing to 1.

5. `main()`: This function serves as the entry point of the program. It checks command-line arguments, executes the crawling process (`crawl`), performs random sampling for PageRank estimation (`sample_pagerank`), and iteratively estimates PageRank values (`iterate_pagerank`). Finally, it prints the results of both sampling and iteration.

## Usage

```$ python pagerank.py PAGEFOLDER```
`PAGEFOLDER` is your folder with pages like `corpus0` `corpus1` `corpus2`