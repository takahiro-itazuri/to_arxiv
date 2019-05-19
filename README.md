# Memo for arXiv submission
## Available or Not
- \input command -> OK, but not recommended.
- include pdf image -> OK

## Errors
### ! LaTeX Error: Option clash for package hyperref.
Comment out hyperref package.
```tex
% \usepackage{hyperref}
```

### ! LaTeX Error: Environment subfigure undefined.
? -> This error is fixed before I knew it.

## Things to Note
- Merge multiple tex files into single tex file.
- Remove unnecessary packages.
- Upload multiple files via tar compression.
- Size limit
	- The size of each file is smaller than 6000 KB.
	- Total size is smaller than 10000 KB.
	- If your submission is oversized, you need to contact with [arxiv](https://arxiv.org/help/sizes).
