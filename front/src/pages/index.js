import React, { useState, useEffect } from 'react';
import {
  Button,
  TextField,
  Paper,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';

function App() {
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState('');

  const listarNotas = async () => {
    try {
      const response = await fetch('http://localhost:5000/notas', {
        method: 'GET',
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data)
        setNotes(data);
      } else {
        console.error('Falha ao buscar notas da API.');
      }
    } catch (error) {
      console.error('Erro ao buscar notas da API:', error);
    }
  };

  const cadastrarNota = async () => {
    if (newNote) {
      try {
        const response = await fetch('http://localhost:5000/cadastrar-nota', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ titulo: newNote, conteudo: '' }),
        });
        if (response.ok) {
          setNewNote('');
          listarNotas(); // Atualiza a lista de notas após o cadastro
        } else {
          console.error('Falha ao cadastrar nota na API.');
        }
      } catch (error) {
        console.error('Erro ao cadastrar nota na API:', error);
      }
    }
  };

  useEffect(() => {
    listarNotas();
  }, []);

  return (
    <div>
      <h1>Lista de Notas</h1>
      <Paper elevation={3} style={{ padding: '16px' }}>
        <TextField
          label="Nova Nota"
          variant="outlined"
          fullWidth
          value={newNote}
          onChange={(e) => setNewNote(e.target.value)}
        />
        <Button variant="contained" color="primary" onClick={cadastrarNota}>
          Adicionar Nota
        </Button>
      </Paper>
      <List>
        {notes.map((note, index) => (
          <ListItem key={index}>
            <ListItemText primary={note[1]} />
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default App;
