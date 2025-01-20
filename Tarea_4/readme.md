# Bootstrap y WAI-ARIA

## Card
No tenía atributos de accesibilidad específicos.
Se añadieron los atributos aria-labelledby y aria-describedby para asociar el título y el texto con su descripción, mejorando la accesibilidad.

```html
<div class="card" style="width: 18rem;" aria-labelledby="title" aria-describedby="text">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title" id="title">Card title</h5>
      <p class="card-text" id="text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>
```

## Switch
No incluía atributos de accesibilidad ni un estado explícito.
Se agregó aria-labelledby al elemento para asociarlo con la etiqueta. También se añadió el atributo checked con un valor inicial (false) y aria-label a la etiqueta para describir su propósito.

```html
<div class="form-check form-switch" aria-labelledby="label">
    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" checked="false" aria-labelledby="label">
    <label class="form-check-label" for="flexSwitchCheckDefault" id="label"  aria-label="Default label">Default switch checkbox input</label>
</div>
```

## Table
Carecía de semántica accesible adicional.
Se añadieron atributos como role="table", role="row", role="columnheader", y role="rowheader para definir mejor la estructura de la tabla. Además, se incluyó aria-labelledby y aria-colspan para describir y estructurar las relaciones entre celdas y encabezados.

```html
<table class="table" role="table" aria-label="table">
    <thead>
      <tr role="row">
        <th scope="col" role="columnheader" id="1" aria-label="Num">#</th>
        <th scope="col" role="columnheader" id="2" aria-label="First">First</th>
        <th scope="col" role="columnheader" id="3" aria-label="Last">Last</th>
        <th scope="col" role="columnheader" id="4" aria-label="Handle">Handle</th>
      </tr>
    </thead>
    <tbody>
      <tr role="row">
        <th scope="row" role="rowheader" aria-labelledby="1">1</th>
        <td aria-labelledby="2">Mark</td>
        <td aria-labelledby="3">Otto</td>
        <td aria-labelledby="4">@mdo</td>
      </tr>
      <tr role="row">
        <th scope="row" role="rowheader" aria-labelledby="1">2</th>
        <td aria-labelledby="2">Jacob</td>
        <td aria-labelledby="3">Thornton</td>
        <td aria-labelledby="4">@fat</td>
      </tr>
      <tr>
        <th scope="row" role="rowheader" aria-labelledby="1">3</th>
        <td colspan="2" aria-colspan="2"  aria-labelledby="2">Larry the Bird</td>
        <td aria-labelledby="4">@twitter</td>
      </tr>  
    </tbody>
  </table>
```

## Tabs
Faltaban atributos para describir mejor las pestañas y su contenido.
Se añadieron role="tablist" para definir el contenedor, role="tab" para las pestañas, y aria-controls para enlazar cada pestaña con su contenido.

```html
<ul class="nav nav-tabs" role="tablist" aria-orientation="horizontal">
    <li class="nav-item">
      <a class="nav-link active" role="tab" aria-controls="tabpanel1" aria-current="page" href="#">Active</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#" role="tab" aria-controls="tabpanel2">Link</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#" role="tab" aria-controls="tabpanel3">Link</a>
    </li>
    <li class="nav-item">
      <a class="nav-link disabled" aria-disabled="true" role="tab" aria-controls="tabpanel4">Disabled</a>
    </li>
  </ul>
```

## Pagination
Sin atributos de accesibilidad detallados.
Se añadió aria-label para describir las acciones de navegación (e.g., "Previous Page"). Además, se incluyó aria-current para marcar la página activa.

```html
<nav aria-label="Page navigation example" role="navigation">
    <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#" aria-label="Previous Page">Previous</a></li>
        <li class="page-item"><a class="page-link" href="#" aria-label="Page 1" aria-current="true">1</a></li>
        <li class="page-item"><a class="page-link" href="#" aria-label="Page 2">2</a></li>
        <li class="page-item"><a class="page-link" href="#" aria-label="Page 3">3</a></li>
        <li class="page-item"><a class="page-link" href="#" aria-label="Next Page">Next</a></li>
    </ul>
</nav>
```