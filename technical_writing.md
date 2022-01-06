# Technical writing

- Technical writing
  - LaTeX
    - Including Source Code in \(\LaTeX\)
  - Markdown
    - Including Source Code in `markdown`

In this class, there will be multiple points at which you will be generating written content. While obviously the content is more important than the presentation, it would be disingenuous to claim presentation doesn't matter. While I suppose you probably could use MS Word or Apple Pages to generate all the written artifacts, the simple truth is neither of those word processors are designed to handle technical or mathematical content. As such, you will be required to make use of one of two alternatives: LaTeX or Markdown.

LaTeX is much more complete, has immense support for a variety of technical notation (from music to chess matches to advanced mathematics and theoretical physics), and is the lingua franca of the scientific writing community. Odds are good most textbooks you've owned were typeset via LaTeX.

Markdown is a newer alternative, with an emphasis on eliminating as much markup as possible. While it can certainly seem esoteric at first (most formatting commands are a single character), it is widely supported, is the default language for README files on GitHub and GitLab, and is relatively easy to use once you get the hang of it. A downside is that there are a variety of mutually incompatible "flavors" of markdown. For the purposes of this class, we will make use of GitHub variants.

## LaTeX

--TODO: Insert video of LaTeX introduction here.

TeX (tau epsilon chi, pronounced like tek) was originally developed by Donald Knuth, supposedly because he was displeased with how his first book in the Art of Computer Programming series was typeset by the publisher. LaTeX was developed by Leslie Lamport as a set of macros and extensions to TeX. You may notice that a lot of HTML tags feel similar or have the same names as LaTeX formatting commands -- this is because the developer of HTML, Sir Tim Berners-Lee (TimBL), was a physicist with a lot of familiarity with LaTeX.

While there are a lot of variants of TeX (AMS-TeX, XeTeX, LaTeX, jadetex, etc.), they are all fundamentally the same tool. TeX Live is the current standard distribution, can be installed in WSL, and is what you should use if you're using LaTeX. I strongly encourage this. A template can be found [here](../assets/template.tex).

If you prefer to use a web browser over VScode (which has immense support for TeX variants), you can also try [Overleaf](https://www.overleaf.com/)(free registration required).

The two best introductions I've been able to find on the web are

- [The Not so Short Introduction to \(\LaTeX\) \(2_\varepsilon\)](https://tobi.oetiker.ch/lshort/lshort.pdf)
- [Learn \(\LaTeX\) in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)

The former is much more comprehensive than the latter, as the latter focuses a lot on the workflow unique to OverLeaf.

LaTeX Workshop in the VScode extensions marketplace is a phenomenal tool for LaTeX, with support for building natively, using a remote server, or even a custom docker image, if that's more your speed. There's an add-on to this called LaTeX Utilities from a different author, that provides formatted paste, among other useful features. See [the wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki) for all the gory details on how to use LaTeX Workshop in VScode.

### Including Source Code in \(\LaTeX\)

Including source code in \(\LaTeX\) is one of those tasks that used to be quite annoying, until someone was motivated to do something about it. About 10 years ago, Konrad Rudolph got really frustrated with the `listings` package, which at the time was the "standard" way to include source code. It suffered from very specific deficiencies:

- No unicode support
- No support for arbitrary string delimiters, as in Ruby
- Manual syntax highlighting styles were required

From these frustrations came the `minted` package. `minted` is vastly simpler to use:

```latex
\begin{minted}{<language>}
<code>
\end{minted}
```

Specify your language, specify the code, and you're off to the races. If you're a markdown user, you might be thinking to yourself "Self, that's very nearly the same as code inclusion in markdown!" And you'd be right -- both were developed roughly concurrently (fenced code blocks were not in the original specification for markdown).

One huge benefit of `minted` is that you can specify a file as the origin of the source code, add line numbers to the output, highlight specific lines or only include specific lines, and even if the code should be inline with the rest of the text. You have full control over where lines will break, what characters are used for indication of a break (both end of line and start of line), and much more.

For more information, please see the [`minted` package documentation](http://tug.ctan.org/tex-archive/macros/latex/contrib/minted/minted.pdf).

## Markdown

--TODO: insert video of Markdown introduction here

As an alternative to LaTeX, markdown has been used by many former students to great success. There are markdown to PDF converters out there, both command line based and as extensions for the popular browsers. While I personally will always prefer LaTeX (inertia is a thing), Markdown works really well and produces decent looking documents, especially if HTML is the target format.

There are some distinct downsides to markdown, first among them the large collection of slightly mismatched variants. For instance, GitLab markdown is distinct from GitHub markdown, which is distinct from R markdown, etc. While the majority of the base functionality is the same, along with a lot of the formatting, there are a lot of incompatible extensions between the various dialects.

While I personally see the above as a major issue with markdown adoption for me personally, ultimately the decision is yours. It is also worth pointing out that many of the markdown renderers also support LaTeX inline with the markdown, so learning both is ultimately the most versatile approach.

Some useful markdown tutorials that I've used:

- [Markdown Here Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet) <- Useful if you use a webmail client
- [GitHub Flavored Markdown](https://github.github.com/gfm/)

### Including Source Code in `markdown`

Markdown source code inclusion is based on the idea of *fenced code blocks*. There are generally two forms:

- Using a single backtick (\`) delimiter before and after the code will put the source code `inline`.
- Using a triple backtick (\`\`\`) delimiter before and after the code will generate a code *block*. This is how the code blocks in this document were created.

In the case of the triple backtick, immediately after the third tick you can specify the language you want to use:

````markdown
```<language>
[source code here]
```
````

While there are github actions for embedding code from a file, I have found no way to natively do so. As I saw a comment on a question regarding markdown:
>The rule of thumb for Markdown is that the answer to 'Can Markdown...' is usually 'Not practically, universally or easily'. – Michael Scheper

Markdown really is great, as far as it goes, but if you really want to control how your document looks, use \(\LaTeX\).
