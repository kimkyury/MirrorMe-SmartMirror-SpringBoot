import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

import '../css/PresentCard.css';

function PresentCardList(props) {
  const presentName = props.name
  const presentImage = props.image;
  return (
    <div className="present-card-list">
      <Card sx={{ maxWidth: 345, backgroundColor: 'blue' }}>
        <CardActionArea>
          <CardMedia
            component="img"
            height="140"
            image={`${presentImage}`}
            alt={`${presentName}`}
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
                {presentName}
            </Typography>
            <Typography variant="body2" color="text.secondary">
                Lizards are a widespread group of squamate reptiles, with over 6,000
                species, ranging across all continents except Antarctica
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </div>
  );
}

export default PresentCardList;