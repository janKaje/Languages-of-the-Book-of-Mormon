## Overview

This is a repository that contains the full text of the Book of Mormon in every spoken language into which it has been fully translated (as long as it is on [churchofjesuschrist.org](https://www.churchofjesuschrist.org/study/scriptures/bofm)). As of yet, there are four languages which almost fit that description but are not on the Church's website, namely Sinhala, Arabic, Western Armenian, and Hebrew. This repository is primarily meant to be an online data source for my other project, Book of Mormon Parallel Reader, but can be used as-is for many other purposes.

Each file has the name of the corresponding 3-letter language code that the Church uses for their website and is saved in JSON format. An index of language names and codes is available under `index.json`. 

Each file contains a dictionary, where the keys are in the format `"<book> <chapter>"` and the values are the full text of the chapter, including titles, headers, summaries, and verse numbers, formatted with BBCode. The BBCode allows for all formatting on the Church's website to be displayed, including Japanese furigana.

Full copyright belongs to the Church of Jesus Christ of Latter-day Saints and Intellectual Reserve.

## Languages yet to be added

### Sinhala
The Church [reported](https://www.churchofjesuschrist.org/study/ensign/2008/12/news-of-the-church/new-products?lang=eng) that the Book of Mormon was being printed in Sinhala in 2008. However, it is not currently on the Church's website, for reasons unknown.

### Arabic
The Church [reported](https://www.churchofjesuschrist.org/study/liahona/1997/06/in-his-own-language?lang=eng) that the Book of Mormon had a 1986 version that was translated into Arabic. However, only up to Helaman 16 is available on the website to read. If we look into the report, though, we can see that several editions were reported, but only had selections. Persian is an example, as it was only fully translated in 2015, but the report points to a 1983 version, which only had selections. It's then reasonable to assume that a full translation into Arabic has yet to be published.

### Western Armenian
The Church has a translation in Eastern Armenian available. A complete Western Armenian translation was printed beginning in 1937, a new translation (selections only) was published in 1983, but after 2018, is out of print and no longer available on the Church's website.

### Hebrew
The Church of Jesus Christ of Latter-day Saints has not translated the Book of Mormon into Hebrew. The only Hebrew translation is printed by the Independent Restoration Branch and not available online.

## Other Issues
The Church's Welsh translation follows the pre-1879 revision chapter and verse breaks, so much of `cym.json` is quite useless and adds lots of bulk to the file, and the rest of it follows a format most modern members of the Church are quite unfamiliar with.

If you're interested in contributing, I would love to hear from you! Open an issue or pull request or send me a message on Discord (@jankaje).