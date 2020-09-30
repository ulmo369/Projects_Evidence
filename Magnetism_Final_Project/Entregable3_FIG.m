function varargout = Entregable3_FIG(varargin)
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Entregable3_FIG_OpeningFcn, ...
                   'gui_OutputFcn',  @Entregable3_FIG_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end

function Entregable3_FIG_OpeningFcn(hObject, eventdata, handles, varargin)
handles.output = hObject;
guidata(hObject, handles);


function varargout = Entregable3_FIG_OutputFcn(hObject, eventdata, handles) 
varargout{1} = handles.output;


% ---FUNCIÓN DE PRIMER SLIDER
function slider1_Callback(hObject, eventdata, handles)
N=400;  %número de espiras
m=2.35; %momento magnético del imán

global b %Se declara para poder utilizarla en diferentes sliders
b=get(hObject, 'Value');%radio de la bobina
set(handles.text1,'String',b*100);%mostrar el valor del slider

flujo=@(z) -10*4*pi*1e-7*m*N*b^2/(2*(b^2+z^2)^(3/2)); %flujo

hold on
fplot(flujo, [-0.1,0.1],'b');%graficar el flujo
hold off

grid on
legend('Flujo','fem')%mostrar el color del flujo

% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% ---FUNCIÓN DEl SEGUNDO SLIDER
function slider2_Callback(hObject, eventdata, handles)
N=400;  %número de espiras
m=2.35; %momento magnético del imán

global b %recive la variable global b

v=get(hObject,'Value');%radio de la bobina
set(handles.text2,'String',v*100);%mostrar el valro del slider


fem= @(z) 3*4*pi*1e-7*m*N*b^2*z*v/(2*(b^2+z^2)^(5/2)); %fem 

hold on
fplot(fem, [-0.1,0.1],'r'); %grafica fem
hold off

xlabel('z(m)'); 
ylabel('V_\epsilon, \Phi')
grid on                         %editar la grafica 
legend('Flujo','fem')
title('Demostraciónde la ley de Faraday')

% --- Executes during object creation, after setting all properties.
function slider2_CreateFcn(hObject, eventdata, handles)
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% ---FUNCIÓN DEl TERCER SLIDER
function slider3_Callback(hObject, eventdata, handles)
Tf=get(hObject,'Value');%radio de la bobina
set(handles.text3,'String',Tf);

% CONDICIONES INICIALES
%Tiempo: 0, z(0) = 10, z'(0)=0
Ti = 0; % Tiempo Inicial
%Tf = 12; % Tiempo Inicial
t =[Ti Tf]; % Vector Tiempo
initial_z = .5; % Altura Inicial - z(t)
initial_dzdt = 0; % Primer derivada - dz/dt
[t, z] = ode45( @fall, t, [initial_z initial_dzdt]);%recive la función

plot(t,z(:,1)); % Displays position

grid on
title('Magnetic Fall')                  %Editar la grafica
xlabel('Tiempo (seconds)'); ylabel('Altura (metros)');

% --- Executes during object creation, after setting all properties.
function slider3_CreateFcn(hObject, eventdata, handles)
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end

%---Funcion para poder sacar la posición
function dzdt=fall(t,x)
m = .01; % Kg
g = 9.81; % aceleration
U = 1000000; % Max Relative permeability for MetGlass
M = 4*pi*(10^-7); % Vacuum permeability
a = .08; % Meters of radio
R = .00009; % Resistivity
f = m*g; % constant 1
k1 = 9*(U*M)^2*(a^4);
k2 = 4*R;
k = k1/k2; % constant 2
dzdt1 = x(2);
dzdt2_1 = k.*x(1).^2;
dzdt2_2 = (x(1) + a).^(5/2);
dzdt2 = -((dzdt2_1.*x(2))./(m.*dzdt2_2)) - f/m + (0*t); % POSITION
dzdt=[dzdt1; dzdt2];


% --- Boton para borrar la grafica
function cl_Callback(hObject, eventdata, handles)
cla(handles.axes1,'reset')
grid on

% ---FUNCIÓN DEl CUARTO SLIDER
function slider4_Callback(hObject, eventdata, handles)
k=get(hObject,'Value');%radio de la bobina
set(handles.text4,'String',k);%mostrar el valor del slider
% Movimiento
x0=zeros(1,2);
x0(1)=10; %valor inicial de x
x0(2)=0; %valor inicial de v; 
tf=10; %tiempo final; 
%k=10; %valor del parámetro 
tspan=[0 tf];
[t,x]=ode45(@caida_iman,tspan,x0, [],k);

plot(t,-x(:,2))  %x(2) es la velocidad
xlabel('tiempo(sec)')
ylabel('velocidad')                     %Editar grafica
grid on
title('Movimiento de un imán en un tubo metálico')

% --- Executes during object creation, after setting all properties.
function slider4_CreateFcn(hObject, eventdata, handles)

if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end

% Función para sacar el movimiento
function a = caida_iman(t,x,k)
a=zeros(2,1);
a(1)=x(2);
n=floor(x(1));  %x(1) posición, x(2) velocidad
temp=0.0;
for j=n-4:n+5 
    temp=temp+(x(1)-j)^2/(1+(x(1)-j)^2)^5;
end
a(2)=-1-k(1)*temp*x(2);
