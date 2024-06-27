import streamlit as st
#from styles.theme import theme


def write():
    #theme()

    st.markdown(
        """
        <style>
            .reportview-container .main .block-container {
                text-align: center;
            }
            .reportview-container p {
                text-align: justify;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='text-align: center; '>Bienvenido a Physical Tools 👋</h1>", unsafe_allow_html=True)

    st.markdown("![Bienvenido](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=358CDFBB&background=FF238200&center=true&random=false&width=700&height=100&lines=%C2%A1%F0%9F%91%8BBienvenido+a++Phisical+Tools+%F0%9F%91%8B!;Tu+aliado+para+análisis+de+datos+sin+complicaciones+..%F0%9F%9A%80)", unsafe_allow_html=True)

    st.markdown("<p style='text-align: justify;'>Tu aliado para análisis de datos sin complicaciones. Nuestra app, construida con Python, te permite calcular y visualizar regresiones lineales y cuadráticas de forma rápida y precisa. Tanto si eres un experto en datos como si estás empezando, nuestra interfaz intuitiva y el poder de Streamlit y scikit-learn te ayudarán a descubrir patrones y tendencias en tus datos.</p>", unsafe_allow_html=True)



    video_file = open('assets/demo_regression.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, autoplay=True,loop=True,muted=True)


    st.header('Grafica generada')
    st.image('assets/demo_grafica.png', caption='Grafica Generada')