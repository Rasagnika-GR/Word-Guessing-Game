import random
import streamlit as st

word_bank = ['treasure', 'precious', 'lover', 'alone', 'bestie']

if "word" not in st.session_state:
    st.session_state.word = random.choice(word_bank)
    st.session_state.guessedWord = ['_'] * len(st.session_state.word)
    st.session_state.attempts = 10
    st.session_state.game_over = False

st.title("🎮 Word Guessing Game")
st.write("Guess the word! You have 10 attempts.")

if not st.session_state.game_over:
    st.write(f"**Current word:** {' '.join(st.session_state.guessedWord)}")
    st.write(f"**Attempts left:** {st.session_state.attempts}")
    
    guess = st.text_input("Enter a letter:", max_chars=1).lower()
    if st.button("Guess"):
        if len(guess) == 1 and guess.isalpha():
            if guess in st.session_state.word:
                for i in range(len(st.session_state.word)):
                    if st.session_state.word[i] == guess:
                        st.session_state.guessedWord[i] = guess
                st.success("✅ Good guess!")
            else:
                st.session_state.attempts -= 1
                st.error("❌ Wrong guess!")
            
            if '_' not in st.session_state.guessedWord:
                st.balloons()
                st.success(f"🎉 You won! The word was: {st.session_state.word}")
                st.session_state.game_over = True
            elif st.session_state.attempts == 0:
                st.error(f"💀 Game Over! The word was: {st.session_state.word}")
                st.session_state.game_over = True
        else:
            st.warning("Please enter ONE letter!")
else:
    if st.button("🔄 New Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
