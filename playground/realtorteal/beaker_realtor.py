from beaker import *
from pyteal import *

from beaker.lib.storage import BoxMapping


# Our custom Struct
class SenderFundsContract(abi.NamedTuple):
    propertyNumber: abi.Field[abi.String]
    Sender: abi.Field[abi.Address]
    Receiver: abi.Field[abi.Address]
    bonusAmount: abi.Field[abi.Uint64]
    startDate: abi.Field[abi.Uint64]
    endDate: abi.Field[abi.Uint64]
    propertySold: abi.Field[abi.Bool]
    haveExpectedSalesPrice: abi.Field[abi.Bool]
    expectedSalesPrice: abi.Field[abi.Uint64]
    meetSalesPrice: abi.Field[abi.Bool]


class SenderFundsStates:
    sender_funds_item = BoxMapping(abi.String, SenderFundsContract)


app = Application("Sender Funds Contract with Beaker", state=SenderFundsStates())


### Add SenderFunds with Boxes ###
@app.external
def createFundsInfo(pay: abi.PaymentTransaction, propertyNumber: abi.String, Receiver: abi.Address, startDate: abi.Uint64, endDate: abi.Uint64, haveExpectedSalesPrice: abi.Bool, expectedSalesPrice: abi.Uint64) -> Expr:
    # purchased = abi.Bool()
    propertySold =  abi.Bool()
    meetSalesPrice  = abi.Bool()
    Sender = abi.Address()
    bonusAmount = abi.Uint64()
    sender_funds_tuple = SenderFundsContract()

    return Seq(
        propertySold.set(Int(0)),
        meetSalesPrice.set(Int(0)),
        Sender.set(Txn.sender()),
        bonusAmount.set(pay.get().amount()),
        sender_funds_tuple.set(propertyNumber, Sender,Receiver, bonusAmount, startDate, endDate, propertySold, haveExpectedSalesPrice, expectedSalesPrice, meetSalesPrice),
        app.state.sender_funds_item[propertyNumber.get()].set(sender_funds_tuple),
    )


### Update SenderFunds Item ###
# @app.external
# def updateSenderFundsItem(item_name: abi.String, *, output: SenderFundsContract) -> Expr:
#     existing_sender_funds_item = SenderFundsContract()
#     new_purchased = abi.Bool()

#     return Seq(
#         existing_sender_funds_item.decode(app.state.sender_funds_item[item_name.get()].get()),
#         new_purchased.set(Int(1)),
#         existing_sender_funds_item.set(item_name, new_purchased),
#         app.state.sender_funds_item[item_name.get()].set(existing_sender_funds_item),
#         app.state.sender_funds_item[item_name.get()].store_into(output),
#     )


### Read SenderFunds Item ###
@app.external
def readItem(item_name: abi.String, *, output: SenderFundsContract) -> Expr:
    return Seq(
        app.state.sender_funds_item[item_name.get()].store_into(output),  
    )

### Withdraw Funds ###
@app.external
def WithdrawFunds(item_name: abi.String, *, output: SenderFundsContract) -> Expr:
    existing_sender_funds_item = SenderFundsContract()
    amount_received = abi.Uint64()
    Receiver = abi.Address()
    return Seq(
        existing_sender_funds_item.decode(app.state.sender_funds_item[item_name.get()].get()),
        amount_received.set(existing_sender_funds_item.bonusAmount),
        Receiver.set(existing_sender_funds_item.Receiver),
        Assert(Receiver.get() == Txn.sender()),
        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.Payment,
                TxnField.receiver: Txn.sender(),
                TxnField.amount: amount_received.get()
            }
        ),
        app.state.sender_funds_item[item_name.get()].store_into(output),  
    )

# @app.external
# def testAllAssert(item_name: abi.String, *, output: abi.Uint64) -> Expr:
#     i = ScratchVar(TealType.uint64)
#     # requestAmount = abi.Uint64()
#     existing_sender_funds_item = SenderFundsContract()
#     existing_sender_funds_item.decode(app.state.sender_funds_item[item_name.get()].get())
#     # output.set(existing_sender_funds_item.bonusAmount)
#     # requestAmount.set(Int(10000000))
#     return Seq(
#         i.store(Int(10000000)),
#         # Assert(output.get() ==  i.load()),
#         # output.set(i.load())
#         output.set(existing_sender_funds_item.bonusAmount)
#     )


    
    


### delete ###
# @app.external
# def deleteSenderFunds(item_name: abi.String) -> Expr:
#     return Pop(app.state.sender_funds_item[item_name.get()].delete())