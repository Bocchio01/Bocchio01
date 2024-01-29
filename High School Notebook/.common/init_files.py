import os

def create_files(file_names, file_contents):
    for name, content in zip(file_names, file_contents):
        with open(name, 'w') as file:
            file.write("% LTeX: language=it\n\n\section{{{}}}\n".format(content))


if __name__ == "__main__":
    file_names = [
        "1.01 - Basics of physics.tex",
        "2.01 - Motions.tex",
        "2.02 - Newton's laws.tex",
        "2.03 - Work.tex",
        "3.01 - The motions of the plane.tex",
        "3.02 - The standard model.tex",
        "3.03 - Gravitational force.tex",
        "3.04 - Momentum and angular momentum.tex",
        "3.05 - Thermology.tex",
        "3.06 - Law of gases.tex",
        "3.07 - Thermodynamics.tex",
        "3.07 - Entropy.tex",
        "4.01 - Harmonic motion.tex",
        "4.02 - Waves.tex",
        "4.03 - Sound.tex",
        "4.04 - Optics.tex",
        "4.05 - Electrostatics.tex",
        "4.06 - Electric current.tex",
        "5.01 - Magnetic field.tex",
        "5.02 - Induced current.tex",
        "5.03 - Inductance.tex",
        "5.04 - Alternating current.tex",
        "5.05 - Maxwell's equations.tex",
        "5.06 - Electromagnetic waves.tex",
        "5.07 - Electromagnetic spectrum.tex",
        "5.08 - Narrow relativity.tex",
        "5.09 - General relativity.tex",
    ]

    content = [
        "Basi della fisica",
        "I moti",
        "Leggi di Newton",
        "Lavoro",
        "I moti del piano",
        "Il modello standard",
        "Forza gravitazionale",
        "Quantità di moto e Momento angolare",
        "Termologia",
        "Legge dei gas",
        "Termodinamica",
        "Entropia",
        "Moto armonico",
        "Le onde",
        "Suono",
        "Ottica",
        "Elettrostatica",
        "Corrente elettrica",
        "Campo magnetico",
        "Corrente indotta",
        "Induttanza",
        "Corrente alternata",
        "Equazioni di Maxwell",
        "Onde elettromagnetiche",
        "Spettro elettromagnetico",
        "Relatività ristretta",
        "Relatività generale",
    ]

    create_files(file_names, content)
