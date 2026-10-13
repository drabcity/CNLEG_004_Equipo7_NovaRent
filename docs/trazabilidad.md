# Trazabilidad: caso de uso -> servicio -> Aggregates -> prueba

| CU | Application Service / Query | Aggregates y Domain Services | Pruebas |
|---|---|---|---|
| CU-01 Entregar vehiculo | `ServicioDeEntrega.entregar_vehiculo` | Vehiculo, ContratoDeRenta (nuevo), Reservacion | `tests/test_cu01_cu02_entrega.py::TestCU01EntregarVehiculo` |
| CU-02 Validar documentacion | `ServicioDeValidacionDeDocumentacion.validar_documentacion_del_conductor` | Reservacion | `tests/test_cu01_cu02_entrega.py::TestCU02ValidarDocumentacion` |
| CU-03 Compensar categoria | `ServicioDeCompensacionDeCategoria.resolver_categoria_no_disponible`; Query `ConsultarOfertaDeCompensacionHandler` | Reservacion + `CompensacionDeCategoria` | `tests/test_cu03_compensacion.py` |
| CU-04 Registrar devolucion | `ServicioDeDevolucion.registrar_devolucion`; Query `ConsultarResumenDeCargosHandler` | ContratoDeRenta + `CalculadoraDeCargosExtra` (3 politicas), Vehiculo | `tests/test_cu04_devolucion.py` |
| CU-05 Limpieza | `ServicioDeLimpieza`; `ManejadorDeMantenimientoMayor`; Query `ConsultarPanelDeVehiculosHandler` | Vehiculo, ContratoDeRenta (cargo retroactivo) | `tests/test_cu05_limpieza.py` |

## Reglas de negocio -> donde viven

| Regla | Codigo |
|---|---|
| Solo un vehiculo Disponible se entrega (N2) | `Vehiculo.entregar` |
| Sin esquema de danos y al menos una foto no se firma (US05) | `ContratoDeRenta.crear` |
| Tarjeta a nombre del titular de la licencia (US12) | `VoucherAbierto.crear` |
| Documentacion invalida: cancela y retiene 10% (US10) | `Reservacion.cancelar_por_documentacion_invalida` |
| Upgrade sin costo, downgrade con 20% de descuento (US03, N4) | `CompensacionDeCategoria` |
| Retraso: 120 min de gracia, 20% por hora, mas de 4 h = dia completo (US04) | `CargoPorRetraso` |
| Combustible = litros x precio + $100 (US06) | `CargoPorCombustibleFaltante` |
| 250 km/dia incluidos, $5 por km extra (US07) | `CargoPorKilometrajeExcedente` |
| Solo "Terminado" deja el vehiculo Disponible (US11) | `Vehiculo.marcar_terminado` |
| Cargo retroactivo por Mantenimiento Mayor (US13) | `ManejadorDeMantenimientoMayor` |
| Solo Administracion cancela cargos (US08) | Fuera de los 5 casos de uso: `CargoExtra.cancelado` existe, pero no hay servicio |
