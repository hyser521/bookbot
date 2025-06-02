def count_words(contents):
    split_contents = contents.split()
    return len(split_contents)

def count_letters(contents):
    counts = {}
    for s in contents:
        l = s.lower()
        if l in counts:
            counts[l] = counts[l] +1
        else:
            counts[l] = 1
    return counts

def sort_on(dict):
    return dict["count"]

def report(letter_counts, total_letters):
    report_list = []
    for key in letter_counts.keys():
        dict = {}
        if key.isalpha():
            dict["char"] = key
            dict["count"] = letter_counts[key]
            report_list.append(dict)
    report_list.sort(reverse=True, key=sort_on)
    report_string = ""
    for dict in report_list:
        report_string += f"{dict["char"]}: {dict['count']}\n"
    ret = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {total_letters} total words
--------- Character Count -------
{report_string}
============= END ==============="""
    return ret