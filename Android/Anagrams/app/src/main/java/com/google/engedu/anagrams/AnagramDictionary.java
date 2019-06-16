/* Copyright 2016 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.engedu.anagrams;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Random;


public class AnagramDictionary {
    private ArrayList<String> wordList;
    private HashSet<String> wordSet;
    private HashMap<String, ArrayList<String>> wordMap;

    private static final int MIN_NUM_ANAGRAMS = 5;
    private static final int DEFAULT_WORD_LENGTH = 3;
    private static final int MAX_WORD_LENGTH = 7;
    private Random random = new Random();

    public AnagramDictionary(Reader reader) throws IOException {
        BufferedReader in = new BufferedReader(reader);
        wordMap = new HashMap<String,ArrayList<String>>();
        wordSet = new HashSet<String>();
        String line;
        wordList = new ArrayList<>();
        while((line = in.readLine()) != null) {
            String word = line.trim();
            wordList.add(word);
            wordSet.add(word);
            String key= sortLetters(word);
            if(wordMap.containsKey(key)) {
               ArrayList<String> anagrams = wordMap.get(key);
               anagrams.add(word);
               wordMap.put(key,anagrams);
            }
            else {
                ArrayList<String> anagrams = new ArrayList();
                anagrams.add(word);
                wordMap.put(key,anagrams);
            }

        }
    }

    public String sortLetters(String word) {
        char[] sortedWord=word.toCharArray();
        Arrays.sort(sortedWord);
        return new String(sortedWord);
    }

    public boolean isGoodWord(String word, String base) {

        /*if(wordSet.contains(word)){
            if (word.contains(base)) {
                return false;
            }
            else{
                return true;
            }
        }*/
        if(!base.contains(word) && wordSet.contains(base)){
            return true;
        }
        return false;

    }

    public List<String> getAnagrams(String targetWord) {
        ArrayList<String> result = new ArrayList<String>();
        String k=sortLetters(targetWord);
        for(String i:wordSet)
            if(k.equals(sortLetters(i)))
                result.add(i);
        return result;
    }

    public List<String> getAnagramsWithOneMoreLetter(String word) {
        ArrayList<String> result = new ArrayList<String>();

        for(char a='a';a<='z';a++){

            String newWord = word + a;
            if(wordMap.containsKey(sortLetters(newWord))){
                ArrayList<String> temp = wordMap.get(sortLetters(newWord));

                for(int i=0;i<temp.size();i++){
                    if(isGoodWord(word,temp.get(i))){
                        result.add(temp.get(i));
                    }
                }
            }
        }
        return result;
    }

    public String pickGoodStarterWord() {
        Random randomizer = new Random();
        String Random = wordList.get(randomizer.nextInt(wordList.size()));
        return Random;
    }
}
