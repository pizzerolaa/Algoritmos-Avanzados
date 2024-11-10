#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <sstream>

using namespace std;

const int INF = numeric_limits<int>::max(); //definimos un valor infinito

//implementamos un BFS para encontrar un camino de aumento en el grafo residual
bool bfs(vector<vector<int>>& rGraph, int s, int t, vector<int>& parent, int n) {
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < n; v++) {
            if (!visited[v] && rGraph[u][v] > 0) {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
                if (v == t)
                    return true;
            }
        }
    }
    return false;
}

//implementamos el algoritmo de Ford-Fulkerson para encontrar el flujo máximo en un grafo
int fordFulkerson(vector<vector<int>>& graph, int s, int t) {
    int n = graph.size();
    vector<vector<int>> rGraph = graph;  //grafo residual
    vector<int> parent(n);
    int max_flow = 0;

    //mientras exista un camino de aumento en el grafo residual
    while (bfs(rGraph, s, t, parent, n)) {
        //encontramos el flujo máximo en el camino de aumento
        int path_flow = INF;
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            path_flow = min(path_flow, rGraph[u][v]);
        }

        //actualizamos las capacidades residuales del grafo
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }

        max_flow += path_flow;  //sumamos el flujo máximo en el camino de aumento
    }

    return max_flow;
}

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vector<vector<int>> capacityMatrix(n, vector<int>(n));
    vector<vector<int>> distanceMatrix(n, vector<int>(n));

    //lemos la primera matriz (capacidades)
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        for (int j = 0; j < n; j++) {
            iss >> capacityMatrix[i][j];
        }
    }

    //leemos la segunda matriz (distancias)
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        for (int j = 0; j < n; j++) {
            iss >> distanceMatrix[i][j];
        }
    }

    //leemos las coordenadas (opcional para futuras modificaciones)
    vector<pair<int, int>> coordinates(n);
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        int x, y;
        sscanf(line.c_str(), "(%d,%d)", &x, &y);
        coordinates[i] = {x, y};
    }

    //calculamos el flujo máximo del nodo 0 al nodo n-1
    int max_flow = fordFulkerson(capacityMatrix, 0, n - 1);

    cout << "El flujo máximo de información del nodo inicial al nodo final es: " << max_flow << endl;

    return 0;
}