#include "./Exo6.hpp"

PileBornee::PileBornee(int capacite)
{
    this->capacite = capacite;
}

bool PileBornee::est_vide()
{
    return this->nb == 0;
}

bool PileBornee::est_pleine()
{
    // 
    return this->nb == this->contenu.size();
}

void PileBornee::empiler(int x)
{
    if(this->est_pleine())
        // error
    this->contenu.push_back(x);
    this->nb ++;
}

void PileBornee::depiler()
{
    if(this->est_vide())
        // error
    //int valeur = this->contenu.;
    return this->contenu.pop_back()
}