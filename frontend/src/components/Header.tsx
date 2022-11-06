import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import {createMuiTheme, MuiThemeProvider} from '@material-ui/core/styles'

const myTheme = createMuiTheme({
  palette: {
    primary: {
      main: "#D30000",
    },
    secondary: {
      main: "#D30000",
    },
  },
});

export const Header: React.FC = () => {
  return (
    <MuiThemeProvider theme={myTheme}>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static" color="inherit">
          <Toolbar>
            {/* <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton> */}
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Raku家事
            </Typography>
            <Button color="inherit">User</Button>
            <Button color="inherit">LogOut</Button>
          </Toolbar>
        </AppBar>
      </Box>
    </MuiThemeProvider>
  );
}
