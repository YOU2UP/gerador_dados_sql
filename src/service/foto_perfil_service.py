import pandas as pd
import random

def gerar_fotos_perfil():
    fotos = []
    possiveis = [
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fs2-techtudo.glbimg.com%2FSSAPhiaAy_zLTOu3Tr3ZKu2H5vg%3D%2F0x0%3A1024x609%2F888x0%2Fsmart%2Ffilters%3Astrip_icc()%2Fi.s3.glbimg.com%2Fv1%2FAUTH_08fbf48bc0524877943fe86e43087e7a%2Finternal_photos%2Fbs%2F2022%2Fc%2Fu%2F15eppqSmeTdHkoAKM0Uw%2Fdall-e-2.jpg&tbnid=xx1BJBlFmLMGzM&vet=12ahUKEwiOpOnrmtuCAxVAmZUCHUPBDa8QMygBegQIARBu..i&imgrefurl=https%3A%2F%2Fwww.techtudo.com.br%2Flistas%2F2023%2F06%2Fdall-e-2-e-mais-8-sites-para-criar-imagem-com-inteligencia-artificial-edsoftwares.ghtml&docid=EE7ip-JrJRQ0lM&w=888&h=528&q=imagens&ved=2ahUKEwiOpOnrmtuCAxVAmZUCHUPBDa8QMygBegQIARBu",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-photo%2Fhandsome-young-muscular-arab-man-600nw-2045195717.jpg&tbnid=fGsb8gxsKYZDcM&vet=12ahUKEwjju7aKm9uCAxV5SLgEHU6cA-sQMygAegQIARA_..i&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fpt%2Fsearch%2Facademia-free&docid=jYrAlLWF3q0nNM&w=600&h=400&itg=1&q=imagens%20academiafree%20use&ved=2ahUKEwjju7aKm9uCAxV5SLgEHU6cA-sQMygAegQIARA_",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Ffotos-gratis%2Fum-homem-negro-bonito-esta-envolvido-em-uma-academia_1157-29805.jpg&tbnid=BfVEO0WhKzouVM&vet=12ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygKegQIARBb..i&imgrefurl=https%3A%2F%2Fbr.freepik.com%2Ffotos-vetores-gratis%2Fpessoa-academia&docid=KP2R--3EjH3ZvM&w=626&h=417&q=imagens%20pessoas%20academia%20free%20use&ved=2ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygKegQIARBb",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1320391277%2Fpt%2Ffoto%2Fprofile-view-powerful-mid-adult-woman-weightlifting-at-gym.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DxlZXPI0twaClITyX8VbiV6XEwaMC412Pp9_TJ-8qmD4%3D&tbnid=RHZpNAuHOiYd4M&vet=12ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygZegQIARB_..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fbr%2Ffotos%2Fmulher-se-exercitando-com-instrutor-de-fitness-de-treino-de-pesos-academia-de-gin%25C3%25A1stica-de-classe&docid=8WnbBkzxX4s4FM&w=612&h=408&q=imagens%20pessoas%20academia%20free%20use&ved=2ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygZegQIARB_",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2F736x%2Fb4%2F7f%2F43%2Fb47f43c8e0a06aced086ae4a6835c726.jpg&tbnid=H74LIB7HumOxOM&vet=12ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygvegUIARCwAQ..i&imgrefurl=https%3A%2F%2Fbr.pinterest.com%2Fpin%2F812829432745381513%2F&docid=cfSHPo_i2OqgwM&w=626&h=417&q=imagens%20pessoas%20academia%20free%20use&ved=2ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMygvegUIARCwAQ",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Ffotos-gratis%2Fjovem-mulher-treinando-na-academia_23-2147915525.jpg%3Fsize%3D626%26ext%3Djpg%26ga%3DGA1.1.386372595.1697500800%26semt%3Dais&tbnid=pNQgt2buyjMpvM&vet=12ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMyhSegUIARCJAg..i&imgrefurl=https%3A%2F%2Fbr.freepik.com%2Ffotos-vetores-gratis%2Facademia-pessoas%2F3&docid=TgbJa3tM7oUTpM&w=626&h=417&itg=1&q=imagens%20pessoas%20academia%20free%20use&ved=2ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMyhSegUIARCJAg",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fuploads.metropoles.com%2Fwp-content%2Fuploads%2F2021%2F03%2F02151707%2Fpexels-jonathan-borba-3076509.jpg&tbnid=_cQUSsL3GVAzKM&vet=12ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMyhhegUIARCrAg..i&imgrefurl=https%3A%2F%2Fwww.metropoles.com%2Fsaude%2Facademia-lotada-veja-5-dicas-para-treinar-intensamente-em-casa&docid=NyyoI8vLyV-cmM&w=960&h=640&q=imagens%20pessoas%20academia%20free%20use&ved=2ahUKEwj9pLmSm9uCAxW4SLgEHW5OC0cQMyhhegUIARCrAg",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fti%2Ffotos-gratis%2Fp1%2F10452997-retrato-de-homem-asiatico-grande-musculo-na-academia-tailandia-pessoas-treino-para-bom-saudavel-treinamento-de-peso-corporal-fitness-na-academia-conceito-foto.jpg&tbnid=BTxHQu6gv5ESTM&vet=10CBcQMyh7ahcKEwig9pakm9uCAxUAAAAAHQAAAAAQBA..i&imgrefurl=https%3A%2F%2Fpt.vecteezy.com%2Ffoto%2F10452997-retrato-de-homem-asiatico-grande-musculo-na-academia-tailandia-pessoas-treino-para-bom-saudavel-treinamento-de-peso-corporal-fitness-na-academia-conceito&docid=z04oaD8oDrDXvM&w=1473&h=980&q=imagens%20pessoas%20academia%20free%20use&ved=0CBcQMyh7ahcKEwig9pakm9uCAxUAAAAAHQAAAAAQBA",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Flistenx.com.br%2Fblog%2Fwp-content%2Fuploads%2F2020%2F01%2Foriginal-81f15d95efad8c272364a18694ef916d.jpeg&tbnid=e6KfbqBS1JCRDM&vet=10CAsQMyjWAWoXChMIoPaWpJvbggMVAAAAAB0AAAAAEAU..i&imgrefurl=https%3A%2F%2Flistenx.com.br%2Fblog%2F7-dicas-para-voce-inovar-na-gestao-de-academia%2F&docid=fBlIpfm7mhhWHM&w=2000&h=1333&q=imagens%20pessoas%20academia%20free%20use&ved=0CAsQMyjWAWoXChMIoPaWpJvbggMVAAAAAB0AAAAAEAU",
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Ffotos-gratis%2Fhomem-atletico-correndo-na-pista-de-corrida-enquanto-se-exercitava-em-uma-academia_637285-8366.jpg%3Fsize%3D626%26ext%3Djpg%26ga%3DGA1.1.1518270500.1698537600%26semt%3Dais&tbnid=qB7N9kdTXl995M&vet=12ahUKEwiq5bbMm9uCAxX7TLgEHbVBBYoQMygWegQIARB2..i&imgrefurl=https%3A%2F%2Fbr.freepik.com%2Ffotos-vetores-gratis%2Ffitness-academia-preto-cinza%2F3&docid=AaQlblIKldbiFM&w=626&h=417&itg=1&q=imagens%20homem%20preto%20academia%20free%20use&ved=2ahUKEwiq5bbMm9uCAxX7TLgEHbVBBYoQMygWegQIARB2"
    ]
    for _ in range(50):
        index = random.randint(0, 9)
        link = possiveis[index] 
        fotos.append(link)
    return fotos

def get_ids():
    ids = list(range(1, 51))
    return ids

def generate_data_frame(fotos, ids):
    df = pd.DataFrame(list(zip(fotos, ids)),
        columns =["url", "usuario_id_usuario"])
    return df

def run():
    fotos = gerar_fotos_perfil()
    ids = get_ids()

    df = generate_data_frame(fotos, ids)
    print(df)
    return df