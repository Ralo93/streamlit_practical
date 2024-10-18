import React, { useEffect, useRef } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const ChordGraph = () => {
  const canvasRef = useRef(null);

  const chords = {
    // [Previous Major, Dominant 7th, Minor 7th, and Diminished chords remain the same...]
    
    // Adding 9th chords
    'A9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'A7': 'Dominant base',
      'D9': 'Fourth progression',
      'E9': 'Fifth progression',
      'Am7': 'Minor relationship'
    }},
    'B9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'B7': 'Dominant base',
      'E9': 'Fourth progression',
      'F#9': 'Fifth progression',
      'Bm7': 'Minor relationship'
    }},
    'C9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'C7': 'Dominant base',
      'F9': 'Fourth progression',
      'G9': 'Fifth progression',
      'Cm7': 'Minor relationship'
    }},
    'D9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'D7': 'Dominant base',
      'G9': 'Fourth progression',
      'A9': 'Fifth progression',
      'Dm7': 'Minor relationship'
    }},
    'E9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'E7': 'Dominant base',
      'A9': 'Fourth progression',
      'B9': 'Fifth progression',
      'Em7': 'Minor relationship'
    }},
    'F9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'F7': 'Dominant base',
      'Bb9': 'Fourth progression',
      'C9': 'Fifth progression',
      'Fm7': 'Minor relationship'
    }},
    'G9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
      'G7': 'Dominant base',
      'C9': 'Fourth progression',
      'D9': 'Fifth progression',
      'Gm7': 'Minor relationship'
    }},
    
    // Original Major chords
    'A': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'A7': 'Dominant extension',
      'D7': 'Fourth progression',
      'E7': 'Fifth progression',
      'F#m7': 'Relative minor',
      'Am7': 'Minor substitution',
      'Adim': 'Diminished tension'
    }},
    'B': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'B7': 'Dominant extension',
      'E7': 'Fourth progression',
      'F#7': 'Fifth progression',
      'G#m7': 'Relative minor',
      'Bm7': 'Minor substitution',
      'Bdim': 'Diminished tension'
    }},
    'C': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'C7': 'Dominant extension',
      'F7': 'Fourth progression',
      'G7': 'Fifth progression',
      'Am7': 'Relative minor',
      'Cm7': 'Minor substitution',
      'Cdim': 'Diminished tension'
    }},
    'D': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'D7': 'Dominant extension',
      'G7': 'Fourth progression',
      'A7': 'Fifth progression',
      'Bm7': 'Relative minor',
      'Dm7': 'Minor substitution',
      'Ddim': 'Diminished tension'
    }},
    'E': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'E7': 'Dominant extension',
      'A7': 'Fourth progression',
      'B7': 'Fifth progression',
      'C#m7': 'Relative minor',
      'Em7': 'Minor substitution',
      'Edim': 'Diminished tension'
    }},
    'F': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'F7': 'Dominant extension',
      'Bb7': 'Fourth progression',
      'C7': 'Fifth progression',
      'Dm7': 'Relative minor',
      'Fm7': 'Minor substitution',
      'Fdim': 'Diminished tension'
    }},
    'G': {'type': 'Major', 'color': '#4CAF50', 'related': {
      'G7': 'Dominant extension',
      'C7': 'Fourth progression',
      'D7': 'Fifth progression',
      'Em7': 'Relative minor',
      'Gm7': 'Minor substitution',
      'Gdim': 'Diminished tension'
    }},
    
    // Dominant 7th chords
    'A7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'D7': 'Fourth resolution',
      'E7': 'Fifth resolution',
      'Am7': 'Minor substitution',
      'D9': 'Extended progression',
      'Adim': 'Diminished tension',
      'A9': 'Extension base'
    }},
    'B7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'E7': 'Fourth resolution',
      'F#7': 'Fifth resolution',
      'Bm7': 'Minor substitution',
      'E9': 'Extended progression',
      'Bdim': 'Diminished tension',
      'B9': 'Extension base'
    }},
    'C7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'F7': 'Fourth resolution',
      'G7': 'Fifth resolution',
      'Cm7': 'Minor substitution',
      'F9': 'Extended progression',
      'Cdim': 'Diminished tension',
      'C9': 'Extension base'
    }},
    'D7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'G7': 'Fourth resolution',
      'A7': 'Fifth resolution',
      'Dm7': 'Minor substitution',
      'G9': 'Extended progression',
      'Ddim': 'Diminished tension',
      'D9': 'Extension base'
    }},
    'E7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'A7': 'Fourth resolution',
      'B7': 'Fifth resolution',
      'Em7': 'Minor substitution',
      'A9': 'Extended progression',
      'Edim': 'Diminished tension',
      'E9': 'Extension base'
    }},
    'F7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'Bb7': 'Fourth resolution',
      'C7': 'Fifth resolution',
      'Fm7': 'Minor substitution',
      'Bb9': 'Extended progression',
      'Fdim': 'Diminished tension',
      'F9': 'Extension base'
    }},
    'G7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
      'C7': 'Fourth resolution',
      'D7': 'Fifth resolution',
      'Gm7': 'Minor substitution',
      'C9': 'Extended progression',
      'Gdim': 'Diminished tension',
      'G9': 'Extension base'
    }},
    
    // Minor 7th chords
    'Am7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Dm7': 'Fourth minor',
      'E7': 'Dominant resolution',
      'A7': 'Dominant substitution',
      'Adim': 'Leading tone connection',
      'A9': 'Extended relationship'
    }},
    'Bm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Em7': 'Fourth minor',
      'F#7': 'Dominant resolution',
      'B7': 'Dominant substitution',
      'B9': 'Extended relationship'
    }},
    'Cm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Fm7': 'Fourth minor',
      'G7': 'Dominant resolution',
      'C7': 'Dominant substitution',
      'C9': 'Extended relationship'
    }},
    'Dm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Gm7': 'Fourth minor',
      'A7': 'Dominant resolution',
      'D7': 'Dominant substitution',
      'D9': 'Extended relationship'
    }},
    'Em7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Am7': 'Fourth minor',
      'B7': 'Dominant resolution',
      'E7': 'Dominant substitution',
      'E9': 'Extended relationship'
    }},
    'Fm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Bbm7': 'Fourth minor',
      'C7': 'Dominant resolution',
      'F7': 'Dominant substitution',
      'F9': 'Extended relationship'
    }},
    'Gm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
      'Cm7': 'Fourth minor',
      'D7': 'Dominant resolution',
      'G7': 'Dominant substitution',
      'G9': 'Extended relationship'
    }},
    
    // Diminished chords remain the same
    'Adim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'A7': 'Dominant resolution',
      'D7': 'Fourth tension',
      'E7': 'Fifth tension',
      'Am7': 'Leading tone resolution'
    }},
    'Bdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'B7': 'Dominant resolution',
      'E7': 'Fourth tension',
      'F#7': 'Fifth tension'
    }},
    'Cdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'C7': 'Dominant resolution',
      'F7': 'Fourth tension',
      'G7': 'Fifth tension'
    }},
    'Ddim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'D7': 'Dominant resolution',
      'G7': 'Fourth tension',
      'A7': 'Fifth tension'
    }},
    'Edim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'E7': 'Dominant resolution',
      'A7': 'Fourth tension',
      'B7': 'Fifth tension'
    }},
    'Fdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'F7': 'Dominant resolution',
      'Bb7': 'Fourth tension',
      'C7': 'Fifth tension'
    }},
    'Gdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
      'G7': 'Dominant resolution',
      'C7': 'Fourth tension',
      'D7': 'Fifth tension'
    }}
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = 1000;
    const height = canvas.height = 1000;
    
    // Clear canvas
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, width, height);

    // Calculate positions
    const nodes = {};
    const chordsList = Object.keys(chords);
    const radius = 400;
    const centerX = width / 2;
    const centerY = height / 2;

    // Position nodes in a circle
    chordsList.forEach((chord, i) => {
      const angle = (i * 2 * Math.PI) / chordsList.length;
      nodes[chord] = {
        x: centerX + radius * Math.cos(angle),
        y: centerY + radius * Math.sin(angle),
        chord: chord,
        type: chords[chord].type,
        color: chords[chord].color
      };
    });

    // Draw connections
    ctx.lineWidth = 0.5;
    ctx.globalAlpha = 0.2;
    Object.entries(chords).forEach(([chord, data]) => {
      Object.keys(data.related).forEach(related => {
        if (nodes[chord] && nodes[related]) {
          ctx.beginPath();
          ctx.moveTo(nodes[chord].x, nodes[chord].y);
          ctx.lineTo(nodes[related].x, nodes[related].y);
          ctx.strokeStyle = data.color;
          ctx.stroke();
        }
      });
    });

    // Draw nodes
    ctx.globalAlpha = 1;
    Object.values(nodes).forEach(node => {
      ctx.beginPath();
      ctx.arc(node.x, node.y, 15, 0, 2 * Math.PI);
      ctx.fillStyle = chords[node.chord].color;
      ctx.fill();
      
      // Draw chord names
      ctx.fillStyle = '#000000';
      ctx.font = '12px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(node.chord, node.x, node.y);
    });

    // Draw legend
    const types = [...new Set(Object.values(chords).map(chord => chord.type))];
    const legendY = 30;
    const legendSpacing = 150;
    
    ctx.textAlign = 'left';
    ctx.font = '14px Arial';
    types.forEach((type, i) => {
      const x = 20 + i * legendSpacing;
      const color = Object.values(chords).find(chord => chord.type === type).color;
      
      ctx.beginPath();