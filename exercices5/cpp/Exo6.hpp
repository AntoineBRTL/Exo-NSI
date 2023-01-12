#include <iostream>
#include <vector>

class PileBornee
{
    private:
        int capacite = 0;
        std::vector<int> contenu;
        int nb = 0;

    public:
        PileBornee(int capacite);

        bool est_vide();

        bool est_pleine();

        void empiler(int x);

        void depiler();
};