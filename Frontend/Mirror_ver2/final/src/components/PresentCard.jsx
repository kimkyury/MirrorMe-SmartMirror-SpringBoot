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
      <Card sx={{ maxWidth: 345, backgroundColor: '#333333' }}>
        <CardActionArea>
          <CardMedia
            component="img"
            height="140"
            image={presentImage}
            alt={presentName}
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="div" style={{ color: 'white' }}>
                {presentName}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </div>
  );
}

export default PresentCardList;