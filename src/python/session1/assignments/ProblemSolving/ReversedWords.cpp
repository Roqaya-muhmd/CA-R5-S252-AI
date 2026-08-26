


//https://www.codewars.com/kata/51c8991dee245d7ddf00000e
#include <bits/stdc++.h>
using namespace std;

string reverse_words(const string& str) {
    string word = "";
    string result = "";
    stack<string> stack_str;

    for (auto s : str) {
        if (s == ' ') {
            if (!word.empty()) {
                stack_str.push(word);
                word = "";
            }
        }
        else {
            word += s;
        }
    }

    if (!word.empty()) {
        stack_str.push(word);
    }

    while (!stack_str.empty()) {
        result += stack_str.top();
        stack_str.pop();

        if (!stack_str.empty()) {
            result += " ";
        }
    }

    return result;
}