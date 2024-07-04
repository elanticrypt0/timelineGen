
""" Este archivo tiene la clase que imprimir el archivo html con la info de las fuentes"""

class HtmlPrinter:
    
    sources=[]
    outputfile_name="resultado.html"
    
    def __init__(self,sources) -> None:
        self.sources=sources
    
    def set_outputfile_name(self,filepath):
        self.outputfile_name=filepath
    
    def generate(self):
        html=self.generate_html_top()
        html+=self.generate_timeline()
        html+=self.generate_html_bottom()
        return html
        
    def save_html(self):
        html_content = self.generate()
        
        # Escribir el contenido en el archivo
        with open(self.outputfile_name, "w", encoding="utf-8") as htmlfile:
            htmlfile.write(html_content)
        
        print(f"Archivo HTML guardado como '{self.outputfile_name}'.")
    
    def generate_timeline(self):
        html_code=f""""""
        for row in self.sources:
            date=row.get_arg_date_format()
            html_code+=f"""
            <li>
                <p class="event-date"><span>{date}</span> <br/> <a class="link" href="{row.link}">{row.title}</a></p>
                <p class="event-description">{row.description}</p>
            </li>
            """
        return html_code
    
    def generate_html_top(self):
        html="""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Línea de tiempo</title>
</head>
<body>
    <h1>Línea de tiempo</h1>
    <ol>
    
        """
        return html
    
    def generate_html_bottom(self):
        html=f"""
    </ol>
    </div>
    {self.generate_css()}
</body>
</html>
        """
        return html
    
    
    def generate_css(self):
        css="""
        <style>
:root {
  font-family: sans-serif;
}
ol {
  margin: 0;
  list-style: none;
  padding: 0;
  --hue: 1;
  --unit: 1rem;
}
h1 {
  text-align: center;
}
p {
  padding-top:5px;
  font-size:0.92em;
  line-height: 1.3;
}
.event-date {
  margin: 0 0 0.25rem;
  font-weight: bold;
}
.event-description {
  margin: 0;
}
li {
  --height: 7rem;
  position: relative;
  display: block;
  background-color: lightblue;
  border-color: lightseagreen;
  padding: 1rem;
  margin: 2rem 0;
  border-radius:5px;
}
li::before {
  content: "";
  background-color: inherit;
  position: absolute;
  display: block;
  width: var(--unit);
  height: var(--unit);
  top: 100%;
  left: calc(50% - (var(--unit)/2));
}
li::after {
  content: "";
  position: absolute;
  display: block;
  top: calc(100% + var(--unit));
  left: calc(50% - (var(--unit)));
  border: var(--unit) solid transparent;
  border-top-color: inherit;
}
li:last-child::before,
li:last-child::after {
  content: none;
}
li:nth-child(20n+1){
  --hue: 1;
}
li:nth-child(20n+2){
  --hue: 2;
}
li:nth-child(20n+3){
  --hue: 3;
}
li:nth-child(20n+4){
  --hue: 4;
}
li:nth-child(20n+5){
  --hue: 5;
}
li:nth-child(20n+6){
  --hue: 6;
}
li:nth-child(20n+7){
  --hue: 7;
}
li:nth-child(20n+8){
  --hue: 8;
}
li:nth-child(20n+9){
  --hue: 9;
}
li:nth-child(20n+10){
  --hue: 10;
}
li:nth-child(20n+11){
  --hue: 11;
}
li:nth-child(20n+12){
  --hue: 12;
}
li:nth-child(20n+13){
  --hue: 13;
}
li:nth-child(20n+14){
  --hue: 14;
}
li:nth-child(20n+15){
  --hue: 15;
}
li:nth-child(20n+16){
  --hue: 16;
}
li:nth-child(20n+17){
  --hue: 17;
}
li:nth-child(20n+18){
  --hue: 18;
}
li:nth-child(20n+19){
  --hue: 19;
}
li:nth-child(20n+20){
  --hue: 20;
}
@media (min-width: 550px) and (max-width: 899px){
  li {
    margin: 1rem;
    width: calc(50% - 4rem);
    float: left;
    min-height: var(--height);
  }
  li:nth-child(4n+3),
  li:nth-child(4n+4) {
    float: right;
  }
  li:nth-child(4n+1)::before {
    top: calc(var(--height)/2 + var(--unit)/2);
    left: 100%;
  }
  li:nth-child(4n+1)::after {
    top: calc(var(--height)/2);
    left: calc(100% + (var(--unit)));
    border: var(--unit) solid transparent;
    border-left-color: inherit;
  }
  li:nth-child(4n+3)::before {
    top: calc(var(--height)/2 + var(--unit)/2);
    left: -1rem;
  }
  li:nth-child(4n+3)::after {
    top: calc(var(--height)/2);
    left: -3rem;
    border: var(--unit) solid transparent;
    border-right-color: inherit;
  }
}
@media (min-width: 900px) and (max-width: 1199px){
  li {
    margin: 1rem;
    width: calc(33.33% - 4rem);
    float: left;
    min-height: 7rem;
  }
  li:nth-child(6n+4),
  li:nth-child(6n+5),
  li:nth-child(6n+6) {
    float: right;
  }
  li:nth-child(6n+1)::before,
  li:nth-child(6n+2)::before {
    top: calc(var(--height)/2 + var(--unit)/2);
    left: 100%;
  }
  li:nth-child(6n+1)::after,
  li:nth-child(6n+2)::after {
    top: 3.5rem;
    left: calc(100% + (var(--unit)));
    border: var(--unit) solid transparent;
    border-left-color: inherit;
  }
  li:nth-child(6n+4)::before,
  li:nth-child(6n+5)::before{
    top: calc(var(--height)/2 + var(--unit)/2);
    left: -1rem;
  }
  li:nth-child(6n+4)::after,
  li:nth-child(6n+5)::after{
    top: calc(var(--height)/2);
    left: -3rem;
    border: var(--unit) solid transparent;
    border-right-color: inherit;
  }
}
@media (min-width: 1200px){
  ol {
    max-width: 1600px;
    margin: 0 auto;
  }
  li {
    margin: 1rem;
    width: calc(25% - 4rem);
    float: left;
    min-height: 7rem;
  }
  li:nth-child(8n+5),
  li:nth-child(8n+6),
  li:nth-child(8n+7),
  li:nth-child(8n+8){
    float: right;
  }
  li:nth-child(8n+1)::before,
  li:nth-child(8n+2)::before,
  li:nth-child(8n+3)::before{
    top: calc(var(--height)/2 + var(--unit)/2);
    left: 100%;
  }
  li:nth-child(8n+1)::after,
  li:nth-child(8n+2)::after,
  li:nth-child(8n+3)::after{
    top: calc(var(--height)/2);
    left: calc(100% + (var(--unit)));
    border: var(--unit) solid transparent;
    border-left-color: inherit;
  }
  li:nth-child(8n+5)::before,
  li:nth-child(8n+6)::before,
  li:nth-child(8n+7)::before {
    top: calc(var(--height)/2 + var(--unit)/2);
    left: -1rem;
  }
  li:nth-child(8n+5)::after,
  li:nth-child(8n+6)::after,
  li:nth-child(8n+7)::after {
    top: calc(var(--height)/2);
    left: -3rem;
    border: var(--unit) solid transparent;
    border-right-color: inherit;
  }
}

span {
      font-size:0.85em;
      color:white;
      padding-bottom:5px;
  }

.link {
    color: #000000;
    text-decoration: underline;
    text-align: right; 
}

.link:hover {
    text-decoration: underline; /* Subrayado al pasar el mouse */
}


</sytle>
        """
        return css
    
    def generate_sign(self):
        html=f"""<a class="link-sign" href="https://github.com/elanticrypt0" target="_blank">by elantycrypt0</a>"""
        return html