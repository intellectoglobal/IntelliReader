import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import AdbIcon from '@mui/icons-material/Adb';
import Signup_img from './assets/Signup.png';
import { Link } from 'react-router-dom';
import React, { ChangeEvent, useState } from 'react';
import Google from './assets/Google.png';
import Facebook from './assets/Facebook.png';
import Divider from '@mui/material/Divider';

const Signup: React.FC = () => {
  const [password, setPassword] = useState<string>('');
  const [confirmPassword, setConfirmPassword] = useState<string>('');

  const handlePasswordChange = (event: ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleConfirmPasswordChange = (event: ChangeEvent<HTMLInputElement>) => {
    setConfirmPassword(event.target.value);
  };

  const passwordsMatch = password === confirmPassword;
  return (
    <Box sx={{marginTop: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', width: '100%'}} >
      <Typography variant="h6" sx={{ fontFamily:'Outfit',fontWeight: 500, fontSize: '40px' }}><AdbIcon sx={{display: 'inline', maxHeight: '100%', maxWidth:'100%', marginRight: '5px'}}/>IntelliReader</Typography>
      <Typography variant='body1' sx={{ fontFamily:'Outfit',letterSpacing: 1.50 ,fontWeight: 100, textShadow: '0px 4px 4px rgba(211, 211, 211, 1)' }}>Join the AI Revolution in PDF Handling Today!</Typography>
      
      <Grid container spacing={2} sx={{marginTop: 6, maxWidth: '80%', height: 'auto', boxShadow: '4px 4px 8px rgba(0, 0, 0, 0.25)',  borderRadius: '16px' }}>
      <Grid item xs={12} sm={6} p={0} sx={{ backgroundColor: '#CAE8FF', borderRadius: '16px 0 0 16px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <Box
            component="img"
            src={Signup_img}
            alt="Sign up"
            sx={{
              maxWidth: '70%',
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <Box
            sx={{
              
              flexDirection: "column",
              marginLeft: "60px",
              marginRight: "70px",
              marginTop: '10px',
              maxWidth: "90%",
              
            }}
          >
            <Typography mt={0} sx={{ textAlign: "left", fontFamily: "Outfit", fontStyle:"Regular", fontSize:"20px", letterSpacing: 1.25 }}>
              Signup to IntelliReader
            </Typography>
            <Typography  mt={2} sx={{ textAlign: "left", fontFamily: "Outfit", fontStyle: 600, fontSize:"10px", color: "#6C6363", letterSpacing: 1.25}}>
              Already have an account ? <Link to="/">Sign In</Link>
            </Typography>
            <Grid container spacing={1} mt={0} justifyContent={'center'}>
              <Grid item xs={6} >
                <Button variant='outlined' fullWidth
                  sx={{
                    marginTop: '10px',
                    
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    height: '51px',
                    color: '#6C6363',
                    textTransform: 'none',
                    
                    
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)',
                    borderRadius: '16px'
                  }}
                >
                  <img src={Google} alt="Google Login" style={{ maxWidth: '30px', marginRight: '20px' }} />
                  <Typography sx={{display: { xs: 'none', sm: 'inline' },fontFamily: 'Outfit',fontSize: '10px', fontWeight: 600, letterSpacing: '1.25px', maxWidth: "100%" }}>Login with Google </Typography>
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button variant='outlined' fullWidth
                  sx={{
                    marginTop: '10px',
                    height: '51px',
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    color: '#6C6363',
                    
                    marginLeft: '10px',
                    maxWidth: '100%',
                    textTransform: 'none',
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)',
                    borderRadius: '16px',
                    
                    
                  }}
                >
                  <img src={Facebook} alt="Facebook Login" style={{ maxWidth: '30px', marginRight: '15px' }} />
                  <Typography sx={{display: { xs: 'none', sm: 'inline' },fontFamily: 'Outfit',fontSize: '10px', fontWeight: 600, letterSpacing: '1.25px', maxWidth: "100%" }}>Login with Facebook</Typography>
                </Button>
              </Grid>
            </Grid>
            <Box sx={{ mt: 0, display: 'flex', justifyContent: 'center', fontSize: '10px', fontWeight: 600, color: '#6C636' }}>
              <Divider sx={{ml: 2,  my: 1, width: '92%', color: '#6C636' }} ><Typography sx={{color:"#6C6363"}}>or</Typography></Divider>
            </Box>
            <Box component="form" noValidate sx={{ mt: -2 }}>
              <TextField
              InputProps={{ sx: { borderRadius: '10px' } }}
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email"
                name="email"
                autoComplete="email"
                autoFocus
                sx={{boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px'}}
              />
              <TextField
                  InputProps={{ sx: { borderRadius: '10px' } }}
                  margin="normal"
                  required
                  fullWidth
                  sx={{boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px'}}
                  id='password'
                  name="password"
                  label="Password"
                  type="password"
                  value={password}
                  onChange={handlePasswordChange}
                 
                  
                />
                <TextField
                  InputProps={{ sx: { borderRadius: '10px' } }}
                  margin="normal"
                  required
                  fullWidth
                  sx={{boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px'}}
                  id='confirm_password'
                  name="confirmPassword"
                  label="Confirm Password"
                  type="password"
                  value={confirmPassword}
                  onChange={handleConfirmPasswordChange}
                  
                  helperText={!passwordsMatch ? 'Passwords do not match' : ''}
                />
              
              <Button
              
                type="submit"
                fullWidth
                variant="contained"
                
                sx={{ mt: 3, mb: 5, boxShadow: '0 4px 8px rgba(0, 0, 0, 0.25)', borderRadius: '10px', backgroundColor: '#2C346B' }}
              >
                Signup
              </Button>
              
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Box>
    
  );
                }
export default Signup;
