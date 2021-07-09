import streamlit as st
import tensorflow as tf
import numpy as np

# Load and prepare text
text = open("corpus/obras.txt", 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))

char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

# Load model
model = tf.keras.models.load_model('model/modelo.h5', compile = False)

# Predictions 
def generate_text(model, start_string):
    
    num_generate = 1000

    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []

    temperature = 0.5

    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        
        predictions = tf.squeeze(predictions, 0)

        predictions = predictions / temperature
        
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
 
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])
    
    text = ''.join(text_generated)
    text = text.rsplit('.', 1)[0]

    return (start_string + text + '.')

# Streamlit
st.title('Gerador de texto de João Guimarães Rosa')
st.write('Inteligência Artficial treinada em todas as obras de João Guimarães Rosa para escrever como o autor')

input_text = st.text_input('Escreva o início da frase:')

if st.button('Gerar texto'):
    generated_text = generate_text(model, start_string = input_text)
    st.write(generated_text)

